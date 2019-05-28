Word=0
Msg=input("Enter Any Message:")
I=0
while I<len(Msg):
	if Msg[I]==" ":
		Word=Word+1
	I=I+1
print("There Are",(Word+1),"Words")