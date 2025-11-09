from QuadBotPortMap import *

async def drive_code():
    await shift(2)
    await use_attachment(-5000, 300)
    await use_attachment(5000, 300)
    await shift(3)
    await use_attachment(-5000, 300)
    await use_attachment(5000, 300)

if __name__ == "__main__": #run on file run but not import
    run_task(drive_code())