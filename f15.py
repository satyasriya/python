class f15:
    def __init__(self,class_start,class_end):
        self.st=class_start
        self.et=class_end
        print("start time:",class_start)
        print("end time:",class_end)
    def lights(self,color):
        print(color)
    def fan(self,speed):
        self.sp=speed
        print(speed)
    def ac(self,ct,ot):
        self.rt=ct
        self.out=ot
        print("room temperature:",ct)
        print("outside temperature:",ot)
    def display(self):
        diff=self.out-self.rt
        print("difference:",diff)
        print(self.sp)
        print(self.st)
        print(self.et)
x=f15(2,3)
x.lights("white")
x.fan(5)
x.ac(26,40)
x.display()
