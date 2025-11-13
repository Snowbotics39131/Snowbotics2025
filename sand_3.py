from QuadBotPortMap import  *


async def drive_code():
    drivebase.settings(straight_speed=175, straight_acceleration=900)
    await shift(3)
    await drivebase.straight(510)
    await run_attachment_stalled(200, 25)
    await use_attachment(225,500)
    await drivebase.straight(-150)
    await drivebase.straight(50)
    await use_attachment(-200,500)
    await drivebase.straight(-390)

run_task(drive_code())
