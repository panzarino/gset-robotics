from PiStorms import PiStorms
from time import sleep
import sys

from ColorSensor import ColorSensor

psm = PiStorms()
c = ColorSensor()

def inroom1():
    psm.led(1, 0, 255, 0)
    sleep(1)
    psm.led(1, 0, 0, 0)

def inroom3():
    psm.led(1, 0, 255, 0)
    sleep(1)
    psm.led(1, 0, 0, 0)

def inroom2():
    psm.led(1, 0, 255, 0)
    sleep(1)
    psm.led(1, 0, 0, 0)

def notinroom2():
    sleep(.5)
    # move forward a bit
    psm.BBM1.setSpeedSync(-40)
    sleep(1.5)
    psm.BBM1.brakeSync()
    sleep(.4)
    # turn left 90 degs
    psm.BBM1.runDegs(-245, 60, True, False)
    psm.BBM2.runDegs(245, 60, True, False)
    sleep(2)
    # go forward until line
    psm.BBM1.setSpeedSync(-40)
    color = c.get_colornum()
    while (color != 4):
        sleep(.1)
        color = c.get_colornum()
    psm.BBM1.brakeSync()
    inroom3()

def notinroom1():
    # hit wall to realign
    psm.BBM1.setSpeedSync(-100)
    while (not psm.BAS2.isTouchedNXT()):
        pass
    sleep(.5)
    psm.BBM1.brakeSync()
    # move backwards until we see the line
    psm.BBM1.setSpeedSync(60)
    sleep(3)
    color = c.get_colornum()
    while ((11 > color or color > 12) and color != 4):
        sleep(.1)
        color = c.get_colornum()
    psm.BBM1.brakeSync()
    if (11 <= color <= 12):
        notinroom2()
    else:
        inroom2()

def house():
    # ram wall
    psm.BBM1.setSpeedSync(-100)
    while (not psm.BAS2.isTouchedNXT()):
        pass
    psm.BBM1.brakeSync()
    # backup
    psm.BBM1.setSpeedSync(60)
    sleep(.2)
    psm.BBM1.brakeSync()
    # turn right 90 degs
    psm.BBM1.runDegs(245, 60, True, False)
    psm.BBM2.runDegs(-245, 60, True, False)
    sleep(2)
    # move forward until see line
    # then decide what to do based off line color
    color = c.get_colornum()
    if (11 > color or color > 12) and color != 4:
        psm.BBM1.setSpeedSync(-40)
    color = c.get_colornum()
    while ((11 > color or color > 12) and color != 4):
        sleep(.1)
        color = c.get_colornum()
    psm.BBM1.brakeSync()
    sleep(.2)
    if (11 <= color <= 12):
        notinroom1()
    else:
        inroom1()
