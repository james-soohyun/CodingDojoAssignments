class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = .15
		else:	
			self.tax = .12

	def displayAll(self):
		print "Price: {} \nSpeed: {} \nFuel: {} \nMileage: {} \nTax: {}\n".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(2000, "35mph", "Full", "15mpg")
car1.displayAll()

car2 = Car(2000, "5mph", "Not Full", "105mpg")
car2.displayAll()

car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
car3.displayAll()

car4 = Car(2000, "25mph", "Full", "25mpg")
car4.displayAll()

car5 = Car(2000, "45mph", "Empty", "25mpg")
car5.displayAll()

car6 = Car(20000000, "35mph", "Empty", "15mpg")
car6.displayAll()