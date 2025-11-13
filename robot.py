import QuadBotPortMap
from pybricks.tools import hub_menu
mission = hub_menu(1,2,3,4,5)
print(mission)

#(forge)_alignment=-----FrontLeft-----15x, 8y_RIGHT
#(M10_KrithvikBlue)_alignment=-----FrontLeft-----14x, 11y_RIGHT
#(CraneMission)_alignment=-----FrontLeft-----
#(TheMostAwesome)_alignment=-----FrontLeft-----
#(sand_3)_alignment=-----FrontLeft-----8x, 1y_LEFT

if mission == 1:
    import forge
if mission == 2:
    import M10_KrithvikBlue
if mission == 3:
    import CraneMission
    run_task(drive_code())
if mission == 4:
    import TheMostAwesome
if mission == 5:
    import sand_3
