from PiStorms import PiStorms
from time import sleep
import sys

from ColorSensor import ColorSensor

psm = PiStorms() # PiStorms object
c = ColorSensor()

def LineFollow():
    exit = False    # break loop
    while (not exit):
        color = c.get_colornum()
        if (8 <= color <= 9):
            exit = True
            psm.led(1, 255, 0, 0)
            psm.BBM1.brakeSync()
            psm.BBM1.brake()
            psm.BBM2.brake()
            sleep(2)
            psm.led(1, 0, 0, 0)
            return
        light = psm.BBS1.lightSensorNXT(True)
        #       520
        error = 540 - light #if within 40 on edge, if negative on line, if positive in white 
        # psm.BBM1.setSpeedSync(30)
        # if (abs(error) < 20): #on edge
        # psm.BBM1.setSpeedSync(30)
        # psm.led(1,0,255,0) #green
        if (error < 0): #on line, turn to right, left wheel accelerate
            psm.BBM1.setSpeed(20)
            psm.BBM2.setSpeed(-40)
        elif (error > 0): #on white, turn to left, right wheel accelerate
            psm.BBM2.setSpeed(20)
            psm.BBM1.setSpeed(-40)
        sleep(0.1)
        if (psm.isKeyPressed()): #exit
            psm.BBM1.brakeSync()
            psm.led(1,0,0,0)
            psm.screen.clearScreen()
            psm.screen.termPrintln("")
            psm.screen.termPrintln("Exiting to menu")
            sleep(0.5)
            exit = True
