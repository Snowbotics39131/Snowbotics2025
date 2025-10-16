from QuadBotPortMap import  *
def drive_code():
    drivebase.straight(150)
    drivebase.turn(-90)
    drivebase.straight(600)
    drivebase.turn(90)
    drivebase.straight(290)
    drivebase.straight(-70)
    drivebase.straight(-70)
    drivebase.straight(-35)
    drivebase.turn(90)
    drivebase.straight(-115)
    drivebase.turn(90)
    drivebase.straight(-170)
    drivebase.straight(250)
    drivebase.turn(90)
    drivebase.straight(450)
    drivebase.turn(-90)
    drivebase.straight(115)
    drivebase.turn(90)
    drivebase.straight(-270)
    drivebase.straight(175)
    drivebase.turn(-90)
    drivebase.straight(-175)
    shift(1)
    use_attachment(-160,1000)

    import IndianaJones


#(5-11)
    


drive_code()

#speaker = hub.speaker
#speaker.volume(100)
#from IndianaJones import *

#run_task(Indiana_Jones(),drive_code())
#multitask(Indiana_Jones(), drive_code())
