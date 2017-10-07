Class NBATeam(object):
	def __init__(self, name, city, color):
		self.name = name
		self.city = city
		self.color = color
		self.players = []

Class Player(object):
	def __init__(self, name, position, jerseyNumber):
		self.name = name
		self.position = position
		self.jerseyNumber = jerseyNumber

GSW = NBATeam("Golden State Warriors", "Oakland", ["blue", "gold"])
GSW.players.append(Player("Stephen Curry", "PG", 30))