class balance:
    def __init__(self):
        self.a=300000
    def display(self,x,y):
        self.a=self.a-x
        self.a=self.a+y
        print("The remaining balance is ",self.a)
