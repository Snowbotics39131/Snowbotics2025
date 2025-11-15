from QuadBotPortMap import  *
def drive_code():
    drivebase.straight(150)
    drivebase.turn(-90)
    drivebase.straight(600)
    drivebase.turn(90)
    drivebase.straight(290)
    drivebase.straight(-70)
    drivebase.straight(-70)
    drivebase.straight(-35)
    drivebase.turn(90)
    drivebase.straight(-115)
    drivebase.turn(90)
    drivebase.straight(-170)
    drivebase.straight(100)
    drivebase.turn(-90)
    shift(2)
    use_attachment(-1350,100)
    drivebase.turn(90)
    drivebase.straight(130)
    drivebase.turn(90)
    drivebase.straight(450)
    drivebase.turn(-90)
    drivebase.straight(115)
    drivebase.turn(90)
    drivebase.straight(-270)
    drivebase.straight(175)
    drivebase.turn(-90)
    hub = InventorHub()
speaker = hub.speaker
speaker.volume(100)

async def Indiana_Jones():
    await speaker.play_notes([
        "E3/5", "F3/16", "G3/8", "C4/2_", "C4/8", "D3/5", "E3/16", "F3/2", "G3/5", "A4/16", "B4/8", "F4/2_", "F4/8", "A4/5", "B4/16", "C4/4", "D4/4", "E4/4",
        "E3/5", "D3/16", "G3/8", "C4/2_", "C4/8", "D4/5", "E4/16", "F4/2", "R/4",
        "G3/5", "G3/16", "E4/4", "D4/5", "G3/16", "E4/4", "D4/5", "G3/16", "E4/4", "D4/5", "G3/16", "E4/8", "D4/8",
        "E3/5", "F3/16", "G3/8", "C4/2_", "C4/8", "D3/5", "E3/16", "F3/2", "G3/5", "A4/16", "B4/8", "F4/2_", "F4/8", "A4/5", "B4/16", "C4/4", "D4/4", "E4/4",
        "E3/5", "D3/16", "G3/8", "C4/2_", "C4/8", "D4/5", "E4/16", "F4/2", "R/4",
        "G3/5", "G3/16", "E4/4", "D4/5", "G3/16", "E4/4", "D4/5", "G3/16", "E4/4", "D4/5", "G3/16", "E4/8", "D4/8",
        "E3/5", "G3/16", "F3/2.", "D3/5", "F3/16", "E3/8", "G3/8", "E4/2",
        "E3/5", "G3/16", "F3/2.", "D3/5", "F3/16", "E3/8", "G3/8", "E4/2", "D4/5", "E4/16", "F4/2.",
        "D4/5", "F4/16", "Eb4/8", "D4/8", "C4/2", "C4/5", "E4/16", "D4/4", "R/8", "G3/8", "D4/4", "C4/5", "B4/16", "C4/2.",
        "E3/5", "G3/16", "F3/2.", "D3/5", "F3/16", "E3/8", "G3/8", "E4/2",
        "E3/5", "G3/16", "F3/2.", "D3/5", "F3/16", "Eb3/8", "D3/8", "C3/2",
        "E3/5", "G3/16", "F3/2.", "D3/5", "F3/16", "E3/8", "G3/8", "E4/2", "D4/5", "E4/16", "F4/4", "R/8",
        "Bb4/8", "F4/4", "Eb4/5", "D4/16", "Eb4/1",
        "F4/4", "R/8", "Bb4/8", "F4/4", "Eb4/5", "D4/16", "Eb4/1",
        "F4/4", "R/8", "Bb4/8", "F4/4", "Eb4/5", "F4/16", "Eb4/4", "R/8", "Ab4/8", "E4/4", "E4/5", "F4/16",
        "G4/1_", "G4/2_", "G4/8", "R/8",
        "E3/5", "F3/16", "G3/8", "C4/4._", "C4/4", "D3/5", "E3/16", "F3/2.",
        "G3/5", "A4/16", "B4/8", "F4/4._", "F4/4", "A4/5", "B4/16", "C4/4", "D4/4", "E4/4",
        "E3/5", "F4/16", "G3/8", "C4/4._", "C4/4", "D4/5", "E4/16", "F4/2", "R/4",
        "G3/5", "G3/16", "E4/4", "D4/5", "G3/16", "E4/4", "D4/5", "G3/16", "E4/4", "D4/5", "G3/16",
        "F4/4", "E4/5", "D4/16", "C4/1_", "C4/1"
    ], tempo=120)


#(5-11)
    


drive_code()

#speaker = hub.speaker
#speaker.volume(100)
#from IndianaJones import *

#run_task(Indiana_Jones(),drive_code())
#multitask(Indiana_Jones(), drive_code())
