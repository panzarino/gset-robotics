from PiStorms import PiStorms
from time import sleep
import sys

psm = PiStorms() # PiStorms object
exit = False    # break loop

while (not exit):
    
	
    if (psm.isPressed() == True): #exit
	psm.BBM1.brakeSync()
	psm.led(1,0,0,0)
	psm.screen.clearScreen()
	psm.screen.termPrintln("")
	psm.screen.termPrintln("Exiting to menu")
	sleep(0.5)
	exit = True

