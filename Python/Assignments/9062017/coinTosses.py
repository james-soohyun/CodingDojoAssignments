import random

def coinToss():
	print "Starting the program..."
	count = 0
	head = 0
	tail = 0
	for i in range(0,5000):
		outcome = round(random.random())
		count+=1
		if outcome == 0:
			head+=1
			print "Attempt #%s: Throwing a coin... It's a head! Got %s head(s) so far and %s tail(s) so far"%(str(count),str(head),str(tail))
		elif outcome == 1:
			tail+=1
			print "Attempt #%s: Throwing a coin... It's a tail! Got %s head(s) so far and %s tail(s) so far"%(str(count),str(head),str(tail))
	print "Ending the program, thank you!"