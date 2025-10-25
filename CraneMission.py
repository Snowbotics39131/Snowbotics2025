from QuadBotPortMap import *
from QuadBotPortMap import drivebase as db

# drivebase.settings(straight_speed=195, straight_acceleration=733, turn_rate=180, turn_acceleration=700)

async def drive_code():
    await db.straight(330)
    await db.turn(90)
    await multitask(db.straight(705),shift(2))
    await db.turn(90)
    await db.straight(175)
    await db.turn(-6)
    await use_attachment(2000, 700)
    await db.straight(-100)

if __name__ == "__main__": #run on file run but not import
    run_task(drive_code())