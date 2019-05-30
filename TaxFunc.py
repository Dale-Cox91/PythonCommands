def Tax(Salary):
	if Salary>20000:
		T=Salary*21/100
	else:
		T=Salary*15/100
	return T

Salary1=int(input("Enter Your Salary: "))
print("Your Tax is:",Tax(Salary1))
print("Your Net Salary is:",(Salary1-Tax(Salary1)))