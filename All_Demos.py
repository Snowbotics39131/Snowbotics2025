import QuadBotPortMap
from pybricks.tools import hub_menu
mission = hub_menu(1,2,3)
print(mission)

if mission == 1:
    import shift
if mission == 2:
    import Omni_Crane_Test
if mission == 3:
    import IndianaJones

