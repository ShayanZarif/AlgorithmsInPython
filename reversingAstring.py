def reverse(string):
	reversed_string = ""
	for i in string:
		reversed_string = i + reversed_string
	print("The reversed form of the string is: " + reversed_string)
myString = "My Name is Shayan"
print("Original form of the string is: " + myString)
reverse(myString)