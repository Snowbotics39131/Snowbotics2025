from PortMap25 import *

async def Indiana_Jones():
    await speaker.play_notes([
        "E4/5", "F4/16", "G4/8", "C5/3", "D4/5", "E4/16", "F4/2", "G4/5", "A5/16", "B5/8", "F5/2", "A5/5", "B5/16", "C5/4", "D5/4", "E5/4", "E4/5", "D4/16"  # long rest to end
    ], tempo=120)

run_task(Indiana_Jones())
#music: https://musescore.com/user/39593079/scores/15831136?srsltid=AfmBOoo-uuN-OR4HRYlrvuquhPlZ7GD4UScxYxLVuZb5AIpy0ZOADF8l
