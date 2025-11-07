from QuadBotPortMap import *
# right 3,1
drivebase.settings(straight_speed=300, straight_acceleration=400)
run_task(shift(1))
drivebase.straight(610)
drivebase.turn(45) #42
drivebase.straight(40)
drivebase.turn(-22) #20
drivebase.straight(-50)
drivebase.turn(-18) #2
drivebase.straight(115)
use_attachment(300,600)
drivebase.turn(-27) #-25
drivebase.straight(-20)
drivebase.turn(-65)
drivebase.straight(-210)
drivebase.straight(370)
drivebase.turn(30)
drivebase.straight(200)
drivebase.turn(-30)
drivebase.straight(230)
drivebase.turn(45)
#run_task(use_attachment(-250, 10000))
drivebase.settings(straight_speed=900, straight_acceleration=900)
drivebase.straight(-245)
drivebase.straight(245)
