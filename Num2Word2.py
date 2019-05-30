def ones(Num):
	Result=""
	if Num==1:
		Result="One"
	if Num==2:
		Result="Two"
	if Num==3:
		Result="Three"
	if Num==4:
		Result="Four"
	if Num==5:
		Result="Five"
	if Num==6:
		Result="Six"
	if Num==7:
		Result="Seven"
	if Num==8:
		Result="Eight"
	if Num==9:
		Result="Nine"
	if Num==10:
		Result="Ten"
	if Num==11:
		Result="Eleven"
	if Num==12:
		Result="Twelve"
	if Num==13:
		Result="Thirteen"
	if Num==14:
		Result="Fourteen"
	if Num==15:
		Result="Fifteen"
	if Num==16:
		Result="Sixteen"
	if Num==17:
		Result="Seventeen"
	if Num==18:
		Result="Eighteen"
	if Num==19:
		Result="Nineteen"
	return Result

def Tens(Num):
	Result=""
	if Num==20:
		Result="Twenty"
	if Num==30:
		Result="Thirty"
	if Num==40:
		Result="Fourty"
	if Num==50:
		Result="Fifty"
	if Num==60:
		Result="Sixty"
	if Num==70:
		Result="Seventy"
	if Num==80:
		Result="Eighty"
	if Num==90:
		Result="Ninety"
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