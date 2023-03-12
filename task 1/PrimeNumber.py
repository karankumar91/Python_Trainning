#write a program check number is prime or not

n=int(input("Enter a number:"))
if n>1:
 for i in range(2,n):
    if (n % i)==0:
        print(n,"its not a prime number")
        break
    else:
        print(n,"its a prime number")
        break
else:
    print(n,"its not a prime number")