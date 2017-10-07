# import random

# bed = random.randint(1,20)
# print bed

class Patient(object):
	id = 0
	def __init__(self, name, allergies):
		self.id = id
		self.name = Patient.id
		self.allergies = allergies
		self.bedNumber = None
		Patient.id+=1

class Hospital(object):
	def __init__(self, name, capacity):
		self.patients = []
		self.name = name
		self.capacity = capacity
		self.beds = self.createBeds()

	def admit(self, patient):
		if len(self.patients)<=self.capacity:
			self.patients.append(patient)
			for i in range(0, len(self.beds)):
				if self.beds[i]["Available"]:
					patient.bedNum = self.beds[i]["bednum"]
					self.beds[i]["Available"] = False
					break
			print "Patient #{} assigned bed #{}".format(patient.id, patient.bedNum)
		else:
			"Hospital is full"

	def discharge(self, patient_id):
		for patient in self.patients:
			if patient.id == patient_id:
				for bed in self.beds:
					if bed["bedNum"] == patient.bedNumber:
						bed["Available"] = True
						break
				self.patients.remove(patient)
				return "Patient #{} discharged. Bed #{} available".format(patient.id, patient.bedNumber)
		return "Patient not found"