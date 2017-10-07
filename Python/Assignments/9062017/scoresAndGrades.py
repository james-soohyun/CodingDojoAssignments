import random

def scoreGrade():
	for count in range(0,10):
		grade = random.randint(60,100)
		if grade<70:
			print "Score: %s; Your grade is D" % (str(grade))
		elif 69<grade<80:
			print "Score: %s; Your grade is C" % (str(grade))
		elif 79<grade< 90:
			print "Score: %s; Your grade is B" % (str(grade))
		elif 89<grade:
			print "Score: %s; Your grade is A" % (str(grade))
	print "End of the program. Bye!"