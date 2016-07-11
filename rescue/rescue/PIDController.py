import time

class PIDController(object):
	""" light sensor has a range from 0 to 1000, motors have power values from 0 to 100 """

	""" simple python PID controller. takes in a read sensor value and then calculates
	a proportional change in motor output that should be applied to a motor[s] to ensure smooth handling
	when following a line. can be modified for more niche purposes later.
	constructor takes in a set point, min motor output, max motor output, and all three PID gains. 
	if you have no idea what to set for set point and the pid gains, set the set point to 500 and
	the gains to 1."""
	def __init__(self, val, minout, maxout, p_gain, i_gain, d_gain):
		self.sp = val               # set set point 
		self.integral = 0
		self.min_ = minout
		self.max_ = maxout
		self.preverr = 0
		self.prevtime = time.time()
		#self.kp = p_gain           # P gain set
                #self.ki = i_gain           # I gain set
		#self.kd = d_gain           # D gain set
		self.setgains(p_gain, i_gain, d_gain)    # set all three gains 
	
	""" calculates error and output iteratively based on sensor readings for motor output.
	pv is the read sensor value.  """
	def calculate(self, pv):    
		curtime = time.time()        # current system time
		dt = curtime - self.prevtime      # get dt
		#err = abs(self.sp - pv)                # error from set point - read value (special case)
		err = self.sp - pv
		self.integral = self.integral + (err * dt)              # Riemann sum
               # err = abs(err)             # must become positive for the algorithm to work
		de = (err - self.preverr) / dt    # gives you de/dt
		self.preverr = err                # track current as prev now
		self.prevtime = curtime           # ...
		""" output manipulated value (3 versions; pick one you think is better, but note that each
		one will require different tuning mechanisms. PID control is on by default.) """
		""" P control only """
		mv = self.kp * err 
		""" PI control (weird) """
		#mv = self.kp * err + self.ki * self.integral
		""" PD control (most common) """
		#mv = self.kp * err + self.kd * de
		""" PID control """
		#mv = (self.kp * err) + (self.ki * self.integral) + (self.kd * de)   
		mv = mv / 10.0           # scaled to proportional motor value change
		if (mv > self.max_):    # output greater than max motor output
			mv = self.max_
		if (mv < self.min_):    # output less than min notor output
			mv = self.min_
		return abs(mv)


	""" sets the PID gains of the contoller """
	def setgains(self, p_gain, i_gain, d_gain):
		self.kp = p_gain
		self.ki = i_gain
		self.kd = d_gain

	""" changes sensor value set point """
	def changesp(self, val):
		self.sp = val

