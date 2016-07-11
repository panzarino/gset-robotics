from PiStorms import PiStorms

from threading import Thread
from time import sleep
import sys

from ColorSensor import ColorSensor
from hand import Hand
from PIDController import PIDController

# psm.BBM1.setSpeedSync(-initspeed)       # initial start
# color sensor will be lined up at around 460-470ish values with the color sensor

victim_search = False
hc = ColorSensor()
psm = PiStorms()

def VictimSearch():
    while (victim_search):
        color = hc.get_colornum()
        if (color == 4):
            psm.led(1, 0, 255, 0)
            sleep(1.5)
            psm.led(1, 0, 0, 0)
            sleep(2.5)
        else:
            sleep(.2)
    return

def LineFollow():
    # declarations
    sp = 580          # sp for line following
    osp_lo = 455         # sp for orienting the robot
    osp_hi = 475
    pcontrol = PIDController(sp, -100, 100, 4.5, 1.3, 0.1) # don't need other two constants
    hand = Hand()
    exit = False
    oriented = False      # if it is ready to enter the house (lined up)
    initspeed = 30
    #hand.open()
    #sleep(2)
    #hand.close()
    #sleep(2)
    #hand.float()
    #sleep(0.5)
    hand.brake()
    global victim_search
    victim_search = True
    victim_thread = Thread(target = VictimSearch)
    victim_thread.start()
    while (not exit):
        sensval = psm.BBS1.lightSensorNXT(True)
        color = hc.get_colornum()
        if (psm.isKeyPressed()): # exit
            exit = True
            victim_search = False
            psm.screen.termPrintln("exiting")
            psm.led(1, 0, 0, 0)
        elif (color >= 8 and color <= 10):
            exit = True
            victim_search = False
            psm.screen.termPrintln("entering house mode")
            psm.led(1, 255, 0, 0)
        # drive control
        elif (sensval < (sp - 15)):     # going to white, right side of line
            mv = pcontrol.calculate(sensval)    # calculate proportion
            #psm.screen.termPrintln(mv)
            psm.BBM2.setSpeed(mv / 2)
            #psm.BBM2.brake()
            psm.BBM1.setSpeed(-mv)        # has to have a sign change
            sleep(0.1)
        elif (sensval > (sp + 15)):     # going to black, left side of right edge
            mv = pcontrol.calculate(sensval)    # calculate proportion
            #psm.screen.termPrintln(mv)
            psm.BBM1.setSpeed(mv / 2)
            #psm.BBM1.brake()
            psm.BBM2.setSpeed(-mv)
            sleep(0.1)
        else:
            psm.BBM1.setSpeedSync(-initspeed)
            sleep(0.1)
	#elif (mv > 0):             # 
        #    psm.BBM2.setSpeed(abs(mv))
        #    psm.BBM1.brake()
        #    sleep(0.1)
        #elif (mv < 0):
        #    psm.BBM1.setSpeed(abs(mv))
        #    psm.BBM2.brake()
        #    sleep(0.1)
    
    # stop the motors at the end
    psm.BBM1.brake()
    psm.BBM2.brake()
    sleep(2)
    psm.led(1, 0, 0, 0)
    # reorient
    """ while (not oriented):
        sensval = psm.BBS1.lightSensorNXT(True)
        color = hc.get_colornum()
        if ( """
