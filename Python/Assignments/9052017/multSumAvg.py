#Multiples
	#Part I
for i in range(0,1001):
	if i%2==1:
		print i

	#Part II
for i in range(5,1000001):
	if i%5==0:
		print i

#Sum List
listA = [1, 2, 5, 10, 255, 3]
sumA = 0
for item in listA:
	sumA+=item
print sumA

#Average List
listB = [1, 2, 5, 10, 255, 3]
sumB = 0
for item in listB:
	sumB+=item
avg = sumB / len(listB)
print avg