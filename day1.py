a=float(input("first number:"))
b=float(input("second number:"))
c=float(input("third number:"))
if (a>b) and (b>c): 
    print("a is greatest")
elif (b>c) and (a<c): 
    print("b is gretest")
else:
    print("c is gretest")

print("your condition is not satisfay")