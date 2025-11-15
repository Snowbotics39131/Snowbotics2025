import QuadBotPortMap
from IndianaJones import *
from pybricks.tools import hub_menu
mission = hub_menu(1,2,3,4,5)
print(mission)

#(forge)_alignment=-----FrontLeft-----15x, 8y_RIGHT
#(M10_KrithvikBlue)_alignment=-----FrontLeft-----14x, 11y_RIGHT
#(CraneMission)_alignment=-----FrontLeft-----XCancelX
#(TheMostAwesome)_alignment=-----FrontLeft-----6x, 7yL
#(sand_3)_alignment=-----FrontLeft-----4x, 1y_LEFT

if mission == 1:
    import forge
if mission == 2:
    import M10_KrithvikBlue
# if mission == 3:
#     import CraneMission
if mission == 3:
    import TheMostAwesome
if mission == 4:
    import sand_3
if mission == 5:
    import mine_cart
if mission == 6:
    run_task(Indiana_Jones())
if mission == 7:
    import Seven_Nation_Army