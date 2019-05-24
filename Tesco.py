Prd=input("What are you Buying?")
Price=input("How much is it?")
Qty=input("How Many Are you buying?")
Amount = float(Price) * int(Qty)
Vat = Amount*15/100
Bill = Amount + Vat
print("Your Bill is as Follows:")
print("Product:",Prd)
print("Amount:",Amount)
print("Vat",Vat)
print("Bill",Bill)