from PiStorms import PiStorms
import sys
from time import sleep

exit = False
psm = PiStorms()

""" reads light values and prints them on the screen """

while (not exit):
    light = psm.BBS1.lightSensorNXT(True)
    if (psm.isKeyPressed()): 
        psm.screen.termPrintln("exit")
        exit = True
    else:
        psm.screen.termPrintln(light)
    sleep(0.1)
