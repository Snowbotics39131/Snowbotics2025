from PortMap25 import *

def align(speed):

    black = 15

    motorLeft.run(speed)
    motorRight.run(speed)

    left_not_aligned = True
    right_not_aligned = True

    while left_not_aligned or right_not_aligned:
        if colorSensorLeft.reflection() < black:
            motorLeft.stop()
            left_not_aligned = False
        if colorSensorRight.reflection() < black:
            motorRight.stop()
            right_not_aligned = False

align(100)