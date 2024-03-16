#create a class of name placements which has a function info which displays the no of placements.
#create a another class named department with function display which will display the names of departments present in the college.
#create a class pragati with a function welcome which displays the msg "welcome to pragati engineering college we are glad"
#pragati class should also display the details about departments and placements.
class placements:
    def info(self):
        print(" 2024 batch 600 placements and still continuing!!")

class department:
    def display(self):
        print("Departments : CSE  IT  MECH CIVIL ECE EEE AIML DS AI")

class pragati(department,placements):
    def welcome(self):
        print("welcome to pragati engineering college we are glad to have you onboard!!")
        self.info()
        self.display()
        
ob=pragati()
ob.welcome()
