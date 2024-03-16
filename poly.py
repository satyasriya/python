#PYTHON DOES NOT SUPPORT FUNCTION OVERLOADING
class arthmetic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
ob=arthmetic()
ob.add(10)
ob.add(40,20)
ob.add(1,2,3)
