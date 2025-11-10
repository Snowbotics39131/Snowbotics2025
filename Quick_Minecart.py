from QuadBotPortMap import *

async def drive_code():
    await drivebase.straight(700)
    await drivebase.turn(-90)
    await multitask(drivebase.straight(800),shift(2))
    await use_attachment(-5000, 300)

if __name__ == "__main__": #run on file run but not import
    run_task(drive_code())

