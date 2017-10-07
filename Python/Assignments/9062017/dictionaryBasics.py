James = {"name": "James", "age": 23, "country of birth": "The United States", "favorite language": "Python"}

def read_dictionary(dictionary):
	for key,data in dictionary.iteritems():
		print "My %s is %s" %(key,data)