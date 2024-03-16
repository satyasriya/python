#write a function which takes two arguments a and b type cast the value of second argument into integer then multiply both the arguments and print the last digit of the result

def typecast(a,b):
    c=int(b)
    p=a*c
    r=p%10
    print(r)
typecast(11,9.3)
typecast(a=11,b=8.3)


#def c(**city):
#    print("city is:",city["pcity"])
#c(pcity="kakinada")
#write a function to calculate sum of first and last digit of a number
