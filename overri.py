#function overriding

class father:
    def bike(self):
        print("harley devidson")
    def laptop(self):
        print("basic configuration")
class child:
    def laptop(father):
        print("advanced configuration")#overriding
ob=child()
ob.bike()
ob.laptop()
