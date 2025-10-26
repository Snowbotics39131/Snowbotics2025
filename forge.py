from QuadBotPortMap import *
drivebase.settings(straight_speed=300, straight_acceleration=400)
shift(1)
drivebase.straight(610)
drivebase.turn(40) #40
drivebase.straight(55)
drivebase.turn(-15) #25
drivebase.straight(-85)
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
drivebase.straight(220)
drivebase.turn(45)

run_task(use_attachment(180, 10000))
wait(1000)

# drivebase.turn(-3)
# drivebase.straight(6)
# drivebase.turn(-15)



