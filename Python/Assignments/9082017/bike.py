class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print "Bike info: Price: {}; Max Speed: {}; Total Miles: {}".format(self.price, self.max_speed, self.miles)
		return self

	def ride(self):
		print "Riding"
		self.miles+=10
		return self

	def reverse(self):
		print "Reversing"
		self.miles-=5
		if self.miles<0:
			self.miles=0
		return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()
bike2 = Bike(200, "25mph")
bike2.ride().ride().reverse().reverse().displayInfo()
bike3 = Bike(200, "25mph")
bike3.reverse().reverse().reverse().displayInfo()