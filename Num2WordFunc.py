def ones(Num):
	Result=""
	Num=[1=="One",2=="Two",3=="Three",4=="Four",5=="Five",6=="Six",7=="Seven",8=="Eight",9=="Nine",10=="Ten",11=="Eleven",12=="Twelve",13=="Thirteen",14=="Fourteen",15=="Fifteen",16=="Sixteen",17=="Seventeen",18=="Eighteen",19=="Nineteen"]
	return Result


def Tens(Num):
	Result=""
	Num=[10=="Ten",20=="Twenty",30=="Thirty",40=="Fourty",50=="Fifty",60=="Sixty",70=="Seventy",80=="Eighty",90=="Ninety"]
	return Result

Number=int(input("Enter any Number: "))
Answer=""
if Number>=1000 and Number<=9999:
	Answer+=ones(int(Number/1000))+"Thousand "
	Number = Number % 1000
if Number>=100:
	Answer+=ones(int(Number/100))+ "Hundred "+"And "
	Number = Number % 100
if Number>=20:
	Answer+=Tens(int(Number/10)*10)
	Number = Number % 10
if Number>0 and Number<=19:
	Answer+=ones(Number)
print(Answer)