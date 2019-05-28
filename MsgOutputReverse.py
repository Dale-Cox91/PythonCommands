Msg=input("Enter any Message: ")
Word=""
I=len(Msg)-1
while I>=0:
	if Msg[I]==" ":
		print(Word)	
		Word=""
	else:
		Word=Msg[I] + Word
	I=I-1
print(Word)