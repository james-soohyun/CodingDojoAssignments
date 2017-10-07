#Odd/Even
def odd_even():
	for count in range(0,2001):
		if count%2==1:
			print 'Number is %s. This is an odd number.' % (str(count))
		elif count%2==0:
			print 'Number is %s. This is an even number.' % (str(count))

#Multiply
def multiply(list, multiplier):
	for count in range(0,len(list)):
		list[count]*=multiplier
	return list

a = [2,4,5]

#Hacker Challenge
def layered_multiples(list):
	print list
	listNew = []
	for x in list:
		val = []
		for i in range(0,x):
			val.append(1)
		listNew.append(val)
	return listNew