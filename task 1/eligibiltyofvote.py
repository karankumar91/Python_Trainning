# crete a program eligibility of vote 

age=int(input("Enter the age:"))
Country=input("Enter the country:")
gender=input("Enter the gender:")

if(age>=18 and Country=="india"):
    print("eligibale for vote:")
elif (age>=21 and Country=="saudi" and gender=="male"):
    print("eligibale for vote:")

elif(age>=18 and Country=="srilanka" and  gender=="male"):
    print("eligibale for vote:")

elif(age>=21 and Country=="srilanka" and gender=="female"):
    print("eligibale for vote:")

else:
    print("not eligibale for vote:")