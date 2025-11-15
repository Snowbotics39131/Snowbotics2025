from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import *

motorLeft = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motorRight = Motor(Port.E, Direction.CLOCKWISE)
motorFrontLeft = Motor(Port.C)
motorFrontRight = Motor(Port.D)
colorSensorLeft = ColorSensor(Port.B)
colorSensorRight = ColorSensor(Port.F)
drivebase = DriveBase(motorLeft,motorRight,56,127.59)
drivebase.use_gyro(True)
