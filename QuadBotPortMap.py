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

#gear=0 is back left gear; gear=1 is back right gear; gear=2 is front left gear; gear=3 is front right gear
async def shift(gear):
    motorShift.reset_angle(None) #reset to value of absolute encoder rather than offset value from PyBricks
    angle = gear * 90 + 45
    motorShift.run_target(500, angle, wait=False)

#clockwise=negative angle; counterclockwise=positive angle
async def  use_attachment(angle, speed):
   await motorAttachment.run_angle(speed, -angle)

async def  use_attachment_async(angle, speed):
   motorAttachment.run_angle(speed, -angle, wait=False)