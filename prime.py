n=int(input("enter a number: "))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("its not a prime number")
else:
    print("its a prime number")




#alternative approach--factors are found upto half of the given number--eg factors of 8 are 1,2,4....factors of 6 are 1,2,3 etc

n=int(input("enter a number: "))
flag=0
for i in range(2,n/2):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("its not a prime number")
else:
    print("its a prime number")
