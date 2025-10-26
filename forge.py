from QuadBotPortMap import *
drivebase.settings(straight_speed=300, straight_acceleration=400)
run_task(shift(1))
drivebase.straight(610)
drivebase.turn(40) #40
drivebase.straight(55)
drivebase.turn(-15) #25
drivebase.straight(-80)
drivebase.turn(-20) #5
drivebase.straight(145)
drivebase.turn(-25) #-20
drivebase.straight(-5)
drivebase.turn(25) #5
drivebase.straight(-20)
drivebase.turn(-95) #-90
drivebase.straight(-200)
wait(100)
drivebase.straight(350)
drivebase.turn(30)
drivebase.straight(200)
drivebase.turn(-30)
drivebase.straight(240)
drivebase.turn(45)
run_task(use_attachment(-300, 10000))
drivebase.straight(-245)


