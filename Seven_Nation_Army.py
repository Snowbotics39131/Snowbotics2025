from QuadBotPortMap import *
from pybricks.parameters import Color

hub.speaker.volume(20)

Seven_Nation_Army = [
    "E4/2", "E4/8_", "G4/4_", "E4/4_", "D4/6_", "C4/2_", "C4/6", "B3/2_", "B3/6","R/4",
    "E4/2", "E4/8_", "G4/4_", "E4/4_", "D4/6_", "C4/4_", "D4/4_", "C4/6_", "B3/2", "R/4",
    "E4/2", "E4/8_", "G4/4_", "E4/4", "E4/6_", "G4/2_", "G4/6", "F#4/2_", "F#4/6", "R/4",
    "E4/2", "E4/8_", "G4/4_", "E4/4", "E4/6_", "G4/4_", "A4/4_", "G4/6_", "F#4/2", "R/4"
]

# Determine color based on notes
def get_color(note):
    if note.startswith("R"):
        return None
    pitch = note.split("/")[0]
    if pitch in ["C4", "C#4", "D4", "D#4"]:
        return Color.RED
    elif pitch in ["E4", "F4", "F#4"]:
        return Color.ORANGE
    elif pitch in ["G4", "G#4", "A4"]:
        return Color.YELLOW
    else:
        return Color.WHITE  # fallback

# Play notes with synced lights
async def SevenNationArmy():
    for note in Seven_Nation_Army:
        color = get_color(note)
        if color:
            hub.light.on(color)
        else:
            hub.light.off()
        await hub.speaker.play_notes([note], tempo=120)

    await hub.light.off()


if __name__ == "__main__": #run on file run but not import
    run_task(SevenNationArmy())