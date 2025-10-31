from QuadBotPortMap import * 
drivebase.straight(   650   )
drivebase.straight(   -120  )
drivebase.straight(    25   )
use_attachment(160,10000)
wait(200)
drivebase.settings(turn_rate=100)
drivebase.turn(-90)