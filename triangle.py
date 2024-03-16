#write a program to check the type of triangle where you take the input from the user for three sides and classify it accordingly into equilateral,isoceles ,scaling(no two sides are equal)

ab= int(input("enter side of triangle:"))
bc= int(input("enter side of triangle:"))
ca= int(input("enter side of triangle:"))
if ab==bc==ca:
       print("equilateral triangle")
elif ab==bc or bc==ca or ab==ca:
      print("isosceles triangle")
else:
    print("scalene triangle")
