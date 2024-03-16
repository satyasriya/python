#check if a given year is a leap year or not
#year is divisible by 4 and not divisible by 100 or if it is divisibleby 400 then it is a leap year


y= int(input("enter year:"))
if y%4==0 and y%100!=0:
    print("leap year")
elif y%400==0:
     print("leap year")
else:
    print("not a leap year")




#simplified code
#y= int(input("enter year:"))
#if (y%4==0 and y%100!=0) or y%400==0:
    #print("leap year")
#else:
    #print("not a leap year")
