def Wordcount(message):
	Word=1
	I=0
	while I<len(message):
		if message[I]==" ":
			Word+=1
		I+=1
	Return Word

print("There are", Wordcount(message),"Words")