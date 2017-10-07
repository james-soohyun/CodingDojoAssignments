#Take a list of strings and string with single character, and print new list of all strings containing character
def findCharacters(list, char):
	newList = []
	for item in list:
		if char in item:
			newList.append(item)
	print newList

word_list = ['hello','world','my','name','is','Anna']
char = 'o'