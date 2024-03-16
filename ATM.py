from module1.bal import balance
from module2.login import auth
class Atm:
    def __init__(self):
        print("Options are:")
        print("1 - Check balance")
        print("2 - Cash withdrawal")
        print("3 - Cash deposit")
        print("4 - Mini statement for past three transactions")
    def choice(self):
        ch= int(input("enter your choice "))
        if ch==1:
                balance.display()
        if ch==2:
                auth.select_card()
                auth.login()
                
        
                
                
                
