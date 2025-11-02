from QuadBotPortMap import *

async def drive_code():
    #shift(2)
    #use_attachment(-150000, 
    drivebase.settings(straight_speed=500)
    #await multitask (drivebase.straight(250), shift(2))
    await shift(2)
    await wait(1000)
    await use_attachment(-700, 600)
    await use_attachment(700, 600)
    


run_task(drive_code())



