#write a function to calculate sum of first and last digit of a number


def sum(n):
    c=n
    while n<0:
        f=n%10
        n=n//10
    l=c%10
    print(f+l)
sum(125697)


##another
def sum(n):
    l=n%10
    while n>10:
        n=n//10
    print(f+l)
sum(785)

