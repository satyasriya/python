class animal:
    def eats(self):
        print("eating")
class bird(animal):
    def fly(self):
        print("flying")
class parrot(bird):
    def body(self):
        print("green")
ob=parrot()
ob.body()
ob.fly()
ob.eats() 
    
