#armstrong number
n=int(input("enter number:"))
count=0
n1=n
d=0
p=0
q=n1
while n>0:
    count=count+1
    n=n//10
while n1>0:
    d=n1%10
    p=p+d**count
    n1=n1//10
if p==q:
    print("armstrong")
else:
    print("not armstrong")

    
