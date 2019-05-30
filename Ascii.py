Alpha=input("Enter Any Character: ")
if ord(Alpha)>=65 and ord(Alpha)<=90:
	print("Upper Case")
else:
	if ord(Alpha)>=97 and ord(Alpha)<=122:
		print("Lower Case")
	else:
		if ord(Alpha)>=48 and ord(Alpha)<=57:
			print("Number")
		else:
			print("Any Other Character")