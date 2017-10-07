def typeList(list):
	sum = 0
	string = "String:"
	sumString = "Sum:"
	for item in list:
		if isinstance(item, int):
			sum+=item
		elif isinstance(item, str):
			string+=item
	if sum > 0 & len(string) > 7:
		print "The list you entered is of a mixed type"
		print string
		print sumString, sum
	if sum == 0 & len(string) > 7:
		print "The list you entered is of string type"
		print string
	if sum > 0 & len(string) == 7:
		print "The list you entered is of integer type"
		print sumString, sum

listX = ['magical unicorns',19,'hello',98.98,'world']
listY = [2,3,1,7,4,12]
listZ = ['magical','unicorns']