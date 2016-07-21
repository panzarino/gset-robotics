from PiStorms import PiStorms
from time import sleep
import sys

psm = PiStorms()

dist1 = 2500
dist2 = 2500
dist3 = 2500
val = 1200
val2 = 400
val3 = 200
val4 = 100

def checkLine():
    if (psm.BBS1.lightSensorNXT(True)<600):
        psm.BBM1.setSpeedSync(100)
        sleep(.3)
        psm.BBM1.runDegs(500, 100, True, False)
        psm.BBM2.runDegs(-500, 100, True, False)
        sleep(.6)

def getAvgDist(): 
    global dist1, dist2, dist3
    dist = psm.BAS2.distanceUSEV3()
    dist3 = dist2
    dist2 = dist1
    dist1 = dist
    return (dist+dist1+dist2+dist3)/4

def turn():
    exit = False
    while (not exit):
        checkLine()
        dist = getAvgDist()
        if (dist > val):
            psm.BBM1.setSpeed(20)
            psm.BBM2.setSpeed(-20)
        else:
            psm.BBM1.brakeSync()
            sleep(.05)
            exit = True
        
        sleep(0.05)
        
        if (psm.isKeyPressed()):
            psm.BBM1.brakeSync()
            psm.led(1,0,0,0)
            psm.screen.clearScreen()
            psm.screen.termPrintln("")
            psm.screen.termPrintln("Exiting to menu")
            sleep(0.5)
            exit = True

def move():
    exit = False
    while (not exit):
        checkLine()
        dist = getAvgDist()
        if (dist < val4):
            psm.BBM1.setSpeed(-100)
            psm.BBM2.setSpeed(-100)
        elif (dist < val3):
            psm.BBM1.setSpeed(-80)
            psm.BBM2.setSpeed(-70)
        elif (dist < val2):
            psm.BBM1.setSpeed(-70)
            psm.BBM2.setSpeed(-55)
        elif (dist < val):
            psm.BBM1.setSpeed(-60)
            psm.BBM2.setSpeed(-40)
        else:
            turn()
        
        sleep(0.05)
        
        if (psm.isKeyPressed()):
            psm.BBM1.brakeSync()
            psm.led(1,0,0,0)
            psm.screen.clearScreen()
            psm.screen.termPrintln("")
            psm.screen.termPrintln("Exiting to menu")
            sleep(0.5)
            exit = True

def main():
    psm.led(1, 0, 255, 0)
    sleep(5)
    psm.led(1, 0, 0, 0)
    turn()
    move()

if __name__ == "__main__":
    main()
