from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import *

hub = InventorHub()

motorLeft = Motor(Port.F, Direction.COUNTERCLOCKWISE)
motorRight = Motor(Port.B, Direction.CLOCKWISE)
motorShift = Motor(Port.D, Direction.CLOCKWISE, reset_angle=False)
motorAttachment = Motor(Port.C, Direction.CLOCKWISE)
colorSensorLeft = ColorSensor(Port.E)
colorSensorRight = ColorSensor(Port.A)
drivebase = DriveBase(motorLeft,motorRight,56,96.5)

drivebase.use_gyro(True)

def shift(gear):
    angle = gear * 90
    motorShift.run_target(100, angle)

def  use_attachment(angle, speed):
    motorAttachment.run_angle(speed, angle)
