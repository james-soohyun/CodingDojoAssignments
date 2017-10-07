name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
	dict = {}
	if len(arr1)==elen(arr2):
		for count in range(0,len(arr1)):
			dict[arr1[count]]=arr2[count]
		return dict
	elif len(arr1)>len(arr2):
		for count in range(0,len(arr1)):
			dict[arr1[count]]=arr2[count]
		return dict
	elif len(arr2)>len(arr1):
		for count in range(0,len(arr2)):
			dict[arr2[count]]=arr1[count]
		return dict