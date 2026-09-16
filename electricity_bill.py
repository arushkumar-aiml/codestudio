unit=int(input("enter the unit:-"))
if unit<=100:
    print("bill amount is:-",unit*5,"rs")
elif unit>=101 and unit <=200:
    print("bill amount is:-",unit*7,"rs")
elif unit >200:
    print("bill amount is:-",unit*10,"rs")
else:
    print("invalid unit")