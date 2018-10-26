def bubblesort(myList):
	for i in range(0,len(myList)-1):
		for j in range(0 , len(myList)-1 - i):
			if myList[j] > myList[j+1] :
				myList[j] , myList[j + 1] = myList[j + 1] , myList[j]

	return myList

alist = ['a' , 's' , 't' , 'b' , 'l' , 'i']
print(bubblesort(alist))