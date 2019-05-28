F=0
Msg=input("Enter your Message: ")
Find=input("What are you looking for? ")
I=0
while I<len(Msg):
	if Msg[I]==Find[0]:
		if Msg[I:I+len(Find)]==Find:
			F=F+1
			I=I+len(Find)-1
	I=I+1
print("There are",F,"instances of this word")