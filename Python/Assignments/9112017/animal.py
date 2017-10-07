class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

	# def __str__(self):
	# 	return "Health: {}".format(self.health)

	def walk(self):
		self.health-=1
		return self

	def run(self):
		self.health-=5
		return self

	def displayHealth(self):
		print "Name: {}\nHealth: {}\n".format(self.name, self.health)

animal1 = Animal("Brandon", 911)
animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		self.name = name
		self.health = 150

	def pet(self):
		self.health+=5
		return self

dog1 = Dog("Henry")
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		self.name = name
		self.health = 170

	def fly(self):
		self.health-=10
		return self

	def displayHealth(self):
		super(Dragon, self).displayHealth()
		print "I am a Dragon"

dragon1 = Dragon("Puff")
dragon1.fly().displayHealth()

animal2 = Animal("Test", 200)
animal2.pet()
animal2.fly()
animal2.displayHealth()

