from PiStorms import PiStorms
from time import sleep

psm = PiStorms()

class Hand(object):
    def open(self):
        # psm.BAM1.runDegs(90, 100, True, False)
        psm.BAM1.setSpeed(100)
        sleep(0.2)
        self.brake()
    def close(self):
        #psm.BAM1.runDegs(-100, 60, True, False)
	psm.BAM1.setSpeed(-60)
        sleep(0.33)
	self.float()
    def brake(self):
        psm.BAM1.brake()
    def float(self):
        psm.BAM1.float()
    def sensed(self):
        return psm.BAS1.isTouchedNXT()
