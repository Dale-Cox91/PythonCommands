Letter=0
Msg=input("Enter Any Message:")
Char=input("What are you looking for?")
I=0
while I<len(Msg):
	if Msg[I]==Char:
		Letter=Letter+1
	I=I+1
print("There Are",(Letter),"characters")