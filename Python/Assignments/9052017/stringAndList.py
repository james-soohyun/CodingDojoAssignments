#Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
words.find("day")
words = words.replace("day", "month")
print words

#Min and Max
x = [2,54,-2,7,12,98]
print "Max of x is", max(x)
print "Min of x is", min(x)

#First and Last
y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y) -1]
newList = [y[0],y[len(y)-1]]
print newList

#New List 
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
list1 = z[:len(z)/2]
print "First half of the list is", list1
list2= z[len(z)/2:]
print "Second half of the list is", list2
list2.insert(0,list1)
print list2