from QuadBotPortMap import *

async def drive_code():
#shift(2)
#use_attachment(-150000, 800)
await drivebase.settings(straight_speed=500)
await multitask (drivebase.straight(250), shift(2))
await use_attachment(70000, 600)
await use_attachment(-70000, 600)
await shift(3)
await use_attachment(-70000, 1000)
await drivebase.turn(45)
await drivebase.straight(100)
await drivebase.turn(90)
await drivebase.straight(150)
await drivebase.turn(-45)
await drivebase.straight(1000)






