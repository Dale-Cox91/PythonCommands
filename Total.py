Phy=input("Enter Marks For Physics:")
Che=input("Enter Marks For Chemistry:")
Mat=input("Enter Marks For Maths:")
Total = int(Phy) + int(Che) + int(Mat)
Per = Total*100/450
print("Total Marks:",Total)
print("------------------------------")
print("Percentage is:",Per)
if Per > 75:
	print("Congratulations, You Passed")
if Per <=75:
	print("I hate you, you failed!!")