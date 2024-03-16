#take a number input from user check if the sum of factors of that number is greater than the original number or not if yes print yes else no (abundant numb or not)
n=int(input("enter a number:"))
fact=0
for i in range(1,n/2):
    if n%i==0:
        fact=fact+i
print(fact)
if fact>n:
    print("yes")
else:
    print("no")
