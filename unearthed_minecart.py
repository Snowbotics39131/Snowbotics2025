from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

from QuadBotPortMap import *

shift(2)
#use_attachment(10000, 100000 )
shift(3)
use_attachment(1000, 100000)

