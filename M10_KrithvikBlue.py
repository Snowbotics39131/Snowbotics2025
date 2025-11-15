from QuadBotPortMap import  *

async def drive_code():
    await multitask(shift(1) , drivebase.straight(150))
    await drivebase.turn(-90)
    await drivebase.straight(610)
    await drivebase.turn(90)
    await drivebase.straight(290)
    await drivebase.straight(-70)
    await drivebase.straight(-70)
    await drivebase.straight(-35)
    await drivebase.turn(90)
    await drivebase.straight(-115)
    await drivebase.turn(90)
    await drivebase.straight(-170)
    await drivebase.straight(250)
    await drivebase.turn(90)
    await drivebase.straight(450)
    await drivebase.turn(-90)
    await drivebase.straight(110)
    await drivebase.turn(90)
    await drivebase.straight(-275)
    await drivebase.straight(175)
    await drivebase.turn(-90)
    await drivebase.straight(-175)
    await use_attachment(-160,500)
    await drivebase.straight(90)
    await drivebase.turn(60)
    drivebase.settings(straight_speed=900, straight_acceleration=900, turn_rate=500, turn_acceleration=500)
    await drivebase.straight(400)

#(5-11)
    


run_task(drive_code())

#speaker = hub.speaker
#speaker.volume(100)
#from IndianaJones import *

#run_task(Indiana_Jones(),drive_code())
#multitask(Indiana_Jones(), drive_code())
