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
def shift(gear):
<<<<<<< HEAD
    motorAttachment.reset_angle(None) #reset to value of absolute encoder rather than offset value from PyBricks
    angle = gear * 90 + 45
=======
    #Shouldn't this be motorShift??
    #motorAttachment.reset_angle(None) #reset to value of absolute encoder rather than offset value from PyBricks
    angle = gear * 90 + 60
>>>>>>> 79946b41e055ba75d4a95d5c5b3d2b20edb6675a
    motorShift.run_target(100, angle)

def  use_attachment(angle, speed):
    motorAttachment.run_angle(speed, angle)
