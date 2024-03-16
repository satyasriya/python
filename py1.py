Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #write a program in which u take an integer input from user if that integer is divisible by 3 and 6 print good number
... #if the integer is divisible by 2 and 7 print avg number , 
... #divisible by 4 0r 9 awesome num else print bad number
... 
... num= int(input("enter a number:"))
... if (num%3==0) and (num%6==0):
...     print("good number")
... elif (num%2==0) and (num%7==0):
...     print("avg number")
... elif (num%4==0) or (num%9==0):
...     print("awesome number")
... else:
