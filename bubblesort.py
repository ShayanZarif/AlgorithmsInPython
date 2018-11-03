
#The below code is used only to describe how this algorithm works.
#The below exact procedure can be done just by using .sort() function.e.g.myList.sort().
#To use the above method to make it sort the list in descending order,
#we have to do   myList.sort(reverse=True).

#This method is only available in Python and JavaScript.(There may be some other languages too.)

def bubblesort(myList):
	for i in range(0,len(myList)-1):
		for j in range(0 , len(myList)-1 - i):
			if myList[j] > myList[j+1] :
				myList[j] , myList[j + 1] = myList[j + 1] , myList[j]

	return myList

alist = ['a' , 's' , 't' , 'b' , 'l' , 'i']
print(bubblesort(alist))

#To make the actual code sort in reverse procedure we have to change the 
#'if myList[j] > myList[j+1]'
#to :
#'if myList[j] < myList[j+1]

