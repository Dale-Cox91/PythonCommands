Msg=input("Enter any Message: ")
Word=""
I=0
while I<len(Msg):
		if Msg[I]==" ":
			print(Word)
			Word=""
		else:
			Word=Word+Msg[I]
		I=I+1
print(Word)