class Call(object):
	id = 0
	def __init__(self, name, phone, time, reason):
		Call.id+=1
		self.id=Call.id
		self.name = name
		self.phone = phone
		self.time = time
		self.reason = reason

	def __str__(self):
		return "Unique ID: {}\nCaller Name: {}\nPhone Number: {}\nTime of call: {}\nReason for Call: {}\n\n".format(self.id, self.name, self.phone, self.time, self.reason)

	def display(self):
		return self

class CallCenter(object):
	def __init__(self):
		self.list = []
		self.queue = len(self.list)

	def add(self, Call):
		self.list.append(Call)
		return self

	def remove(self):
		# for i in range(0,len(self.list)-1):
		# 	self.list[i]=self.list[i+1]
		self.list.pop(0)
		return self

	def info(self):
		for Call in self.list:
			print "Name: {}\nPhone Number: {}\n".format(Call.name, Call.phone)
		return self

	def removeIndex(self, phone):
		for Call in self.list:
			if Call.phone == phone:
				self.list.remove(Call)
		return self


call1 = Call("James",9257860042,"6:04PM","test")
call2 = Call("Emergency",911,"6:05PM","test2")
call3 = Call("Hello",2309134,"6:54PM","test3")


center1 = CallCenter()
center1.add(call1).add(call2).add(call3).info()
center1.removeIndex(911).info()