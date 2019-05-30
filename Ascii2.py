Alpha=input("Enter any Message: ")
if ord(chr(Alpha))>=68 and ord(chr(Alpha))<=90:
	print(chr(ord(Alpha)+32))
else:
	if chr(ord(Alpha))>=91 and chr(ord(Alpha))<=122:
		print(chr(ord(Alpha)-32))