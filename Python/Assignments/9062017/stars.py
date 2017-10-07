x = [4,6,1,3,5,7,25]

def draw_stars(list):
	for item in list:
		if isinstance(item, int):
			print "*"*item
		elif isinstance(item, str):
			print item[0].lower()*len(item)

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]