class Superhero():
	def __init__(self,name,city,powers):
		self.name=name
		self.city=city
		self.powers=powers

	def talk(self):
		print "I'm Batman"
		return self

newHero = Superhero("Brandon","Spanaway","telekinesis")
print newHero

batman = Superhero("Batman", "Gotham", "rich")
batman.talk()
batman.talk().talk()

class Villain():
	def __init__(self,name,city,powers):
		self.name=name
		self.city=city
		self.powers=powers

newVillain = Villain("Hanh","Everett","racism")
print newVillain