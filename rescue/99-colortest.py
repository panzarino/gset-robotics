from PiStorms import PiStorms
from time import sleep
from rescue.ColorSensor import ColorSensor

print "running program"
psm = PiStorms()
hc = ColorSensor()

#exit variable will be used later to exit the program and return to PiStorms
exit = False

# Used to only print when needed
color = 0

# My Sensor was in BBS1.  Adjust as needed
psm.BBS2.activateCustomSensorI2C()

while(not exit):
  color = hc.get_colornum()
  # msg = "Color Number:" + str(color)
  # psm.screen.clearScreen()
  # psm.screen.drawAutoText(msg, 15, 164, fill=(255, 255, 255), size = 18)
  psm.screen.termPrintln(color)

  if(psm.isKeyPressed() == True): # if the GO button is pressed
    psm.screen.clearScreen()
    psm.screen.termPrintln("")
    psm.screen.termPrintln("Exiting to menu")
    sleep(0.5)
    exit = True

  sleep(0.25)

