#take an integer as an input from the user and check whether if the number is divisible by sum of digits or not... 
n=int(input("enter a number:"))
s=0
q=n
while n>0:
    b=n%10
    s=s+b
    n=n//10
if q%s==0:
    print("divisible")
else:
    print("not divisible")
    
