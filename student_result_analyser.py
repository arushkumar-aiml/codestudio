marks=int(input("enter the marks:-"))

if marks<=100 and marks >=80:
    print("grade A")
elif marks<=80 and marks>=60:
    print("grade B")
if marks<=60 and marks>=40:
    print("grade C")
elif marks<0 or marks>100:
    print("invalid marks")
else:
    print("fail")


