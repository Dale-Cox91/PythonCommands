Numbers=[]
while True:
	Num=int(input("Enter any Number here: "))
	if Num==0:
		break
	else:
		Numbers.append(Num)
Highest=Numbers[0]
i=1
while i<len(Numbers):
	if Numbers[i]>Highest:
		Highest=Numbers[i]
	i+=1
print("The Highest Number is: ",Highest)