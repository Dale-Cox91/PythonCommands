Name=input("Enter Your Name Here:")
Salary=int(input("How much do you Earn?"))
if Salary>5000:
	Tax = Salary*20/100
else:
	Tax = Salary*15/100
NetSal = Salary-Tax
print("Name:",Name)
print("Salary:",Salary)
print("Tax",Tax)
print("Net Salary:",NetSal)