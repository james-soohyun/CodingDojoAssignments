class User(object):
	def __init__(self, id, name):
		self.id = id
		self.name = name

class Db(object):
	def __init__(self):
		self.contents = []
		self.next_id = 1

	def create(self, name):
		self.contents.append(User(self.next_id, name))
		self.next_id+=1
		return self

	def all(self):
		for user in self.contents:
			print user.name, user.id
		return self.contents

	def get(self, id):
		for user in self.contents:
			if user.id == id:
				return user
			else:
				return None

	def filter(self, name):
		names = []
		for user in self.contents:
			if user.name == name:
				names.append(name)
		return names

	def exclude(self, name):
		names = []
		for user in self.contents:
			if user.name != name:
				names.append(name)
		return names



UserDB = Db()
UserDB.create("Joey").create("James").create("Jon")
print UserDB.all()
print UserDB.get(1)
print UserDB.exclude("Joey")
print UserDB.filter("Joey")