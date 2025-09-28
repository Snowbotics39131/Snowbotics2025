#Align at (5, 1) on the red side.
#Reliablility is a bit dubious, but not much more so than anything else.
def wait_for_button():
    while not hub.buttons.pressed():
        pass
def sideways_prongs_forward():
    motorAttachment.run_until_stalled(360, duty_limit=65)
def curved_things_forward():
    motorAttachment.run_until_stalled(-360, duty_limit=65)
from QuadBotPortMap import *
shift(2)
sideways_prongs_forward()
drivebase.straight(595)
drivebase.straight(-160)
curved_things_forward()
use_attachment(90, 260)
drivebase.settings(straight_speed=120)
drivebase.straight(80)
#use_attachment(60, 360)
sideways_prongs_forward()
drivebase.settings(straight_speed=500)
drivebase.straight(-700)