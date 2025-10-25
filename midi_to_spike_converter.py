# midi_to_spike_converter.py
# Run this on your computer: pip install mido
# Usage: python midi_to_spike_converter.py yourfile.mid > output.py
# Then copy output.py to Spike Prime hub and run it.

import mido
import sys

def midi_note_to_spike_note(midi_note):
    """Convert MIDI note number (0-127) to Spike note name like 'C4'."""
    if midi_note < 0 or midi_note > 127:
        return None
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    pitch_class = midi_note % 12
    octave = (midi_note // 12) - 1
    if octave < 2 or octave > 8:
        print(f"Warning: Note {midi_note} (octave {octave}) out of Spike range (2-8), skipping.")
        return None
    return notes[pitch_class] + str(octave)

def beats_to_duration(beats):
    """Approximate beat duration to Spike note length string like '4' or '8.'."""
    if beats <= 0.05:  # Skip very short
        return None
    length_options = [
        (6, '1.'),   # Whole dotted
        (4, '1'),    # Whole
        (3, '2.'),   # Half dotted
        (2, '2'),    # Half
        (1.5, '4.'), # Quarter dotted
        (1, '4'),    # Quarter
        (0.75, '8.'),# Eighth dotted
        (0.5, '8'),  # Eighth
        (0.375, '16.'), # Sixteenth dotted
        (0.25, '16'), # Sixteenth
        (0.125, '32') # Thirty-second
    ]
    closest = min(length_options, key=lambda x: abs(x[0] - beats))
    diff = abs(closest[0] - beats)
    if diff > 0.125:
        print(f"Warning: {beats:.3f} beats approximated to {closest[0]:.3f} beats (diff {diff:.3f}).")
    return closest[1]

def convert_midi_to_spike(filename):
    try:
        mid = mido.MidiFile(filename)
    except Exception as e:
        print(f"Error loading MIDI: {e}")
        return None
    
    ticks_per_beat = mid.ticks_per_beat
    # Use first track or merge for simplicity; adjust if multi-track needed
    track = mido.merge_tracks([t for t in mid.tracks if any(msg.type in ['note_on', 'note_off'] for msg in t)])
    
    notes_str = []
    current_time = 0.0
    active_notes = {}  # Handle basic polyphony by sequentializing
    last_end_time = 0.0
    tempo = 500000  # Default 120 BPM
    bpm = 120
    tempo_changed = False
    
    for msg in track:
        current_time += msg.time
        
        if msg.type == 'set_tempo':
            tempo = msg.tempo
            bpm = round(mido.tempo2bpm(tempo))
            if tempo_changed:
                print("Warning: Tempo changes detected; using final BPM.")
            tempo_changed = True
        
        if msg.type == 'note_on' and msg.velocity > 0:
            # Close previous notes if polyphony
            for note in list(active_notes.keys()):
                if note != msg.note:
                    start = active_notes[note]
                    dur_beats = (current_time - start) / ticks_per_beat
                    dur_str = beats_to_duration(dur_beats)
                    if dur_str:
                        note_name = midi_note_to_spike_note(note)
                        if note_name:
                            notes_str.append(f'"{note_name}/{dur_str}"')
                    del active_notes[note]
                    last_end_time = max(last_end_time, current_time)
            
            # Add rest for gap
            gap_beats = (current_time - last_end_time) / ticks_per_beat
            if gap_beats > 0:
                rest_str = beats_to_duration(gap_beats)
                if rest_str:
                    notes_str.append(f'"R/{rest_str}"')
            
            active_notes[msg.note] = current_time
        elif (msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0)):
            if msg.note in active_notes:
                start = active_notes[msg.note]
                dur_beats = (current_time - start) / ticks_per_beat
                dur_str = beats_to_duration(dur_beats)
                if dur_str:
                    note_name = midi_note_to_spike_note(msg.note)
                    if note_name:
                        notes_str.append(f'"{note_name}/{dur_str}"')
                last_end_time = max(last_end_time, current_time)
                del active_notes[msg.note]
    
    # Close remaining notes
    for note, start in active_notes.items():
        dur_beats = (current_time - start) / ticks_per_beat
        dur_str = beats_to_duration(dur_beats)
        if dur_str:
            note_name = midi_note_to_spike_note(note)
            if note_name:
                notes_str.append(f'"{note_name}/{dur_str}"')
    
    if not notes_str:
        print("No valid notes found.")
        return None
    
    notes_list_str = '[' + ', '.join(notes_str) + ']'
    
    # Generated MicroPython code for Spike Prime (uses only built-in 'spike' module)
    code = f'''from QuadBotPortMap import *

hub.speaker.volume(100)  # Adjust volume 0-100 as needed

async def play_melody():
    await hub.speaker.play_notes({notes_list_str}, tempo={bpm})

if __name__ == "__main__": #run on file run but not import
    run_task(play_melody())
'''
    return code

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python midi_to_spike_converter.py <file.mid>")
        sys.exit(1)
    filename = sys.argv[1]
    code = convert_midi_to_spike(filename)
    if code:
        print(code)
        print("# Generated MicroPython code for Spike Prime.")
        print("# Copy-paste into a .py file on the hub and run.")
        print("# It uses only Spike's built-in modules: no external imports needed.")
    else:
        print("Conversion failed.")