#calculate the difference of sum of numbers that are divisible by 6 and not divisible by 6 in the range of first 30 numbers
fact=0
b=0
for i in range(1,31):
    if i%6==0:
        fact=fact+i
    else:
        b=b+i
if fact>b:
    print(fact-b)
else:
    print(b-fact)
        
