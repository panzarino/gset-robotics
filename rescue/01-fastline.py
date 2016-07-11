from PiStorms import PiStorms
from time import sleep
import sys

psm = PiStorms() # PiStorms object
exit = False    # break loop

while (not exit):
    light = psm.BBS1.lightSensorNXT(True)
    #       520
    error = 540 - light #if within 40 on edge, if negative on line, if positive in white 
    # psm.BBM1.setSpeedSync(30)
    # if (abs(error) < 20): #on edge
	# psm.BBM1.setSpeedSync(30)
	# psm.led(1,0,255,0) #green
    if (error < 0): #on line, turn to right, left wheel accelerate
  	psm.BBM1.setSpeed(25)
	psm.BBM2.setSpeed(-50)
	psm.led(1,0,0,255)#blue
    elif (error > 0): #on white, turn to left, right wheel accelerate
	psm.BBM2.setSpeed(25)
	psm.BBM1.setSpeed(-50)
	psm.led(1,255,0,0)#Red
    sleep(0.1)

    if (psm.isKeyPressed()): #exit
        psm.BBM1.brakeSync()
	psm.led(1,0,0,0)
	psm.screen.clearScreen()
	psm.screen.termPrintln("")
	psm.screen.termPrintln("Exiting to menu")
	sleep(0.5)
	exit = True
