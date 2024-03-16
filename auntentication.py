import remainabalance as rem
z=rem.balance()
class auntentication:
    x=[]
    l=[]
    def cardselction(self):
        print("please select card te following cards")
        self.card=input("please select card from  following cards:Rupay,Visa,Master:")
    def authentication(self):
        user=input("Enter the username:")
        passw=input("Enter the password:")
        self.k=0
        while(user!=passw):
            print("invalid login!,login three chances!,please enter agaian:")
            user=input("Enter the username:")
            passw=input("Enter the password:")
        self.k=1
        print("login successfull")
    def checkbalance(self,a=20000):
        self.bal=a
        print("The availble balance in this acount is",self.bal)
    def cashwith(self):
        if(self.card in ["Rupay","1"]):
            w1=int(input("Enter the amount to be wthdrawed:"))
            if(w1>2000):
                w1=int(input("Enter the amount within 2000:"))
        if(self.card in ["Visa","2"]):
             w1=int(input("Enter the amount to be wthdrawed:"))
             if(w1>5000):
                 w1=int(input("Enter the amount within 5000:"))
        if(self.card in ["Master","3"]):
             w1=int(input("Enter the amount to be wthdrawed:"))
             if(w1>8499):
                 w1=int(input("Enter the amount within 8499:"))
        a=self.bal-w1
        self.checkbalance(a)
        self.x.append("w")
        self.l.append(w1)
        z.display(w1,0)
    def depos(self):
        w2=int(input("Enter the amount to be deposited:"))
        a=self.bal+w2
        self.checkbalance(a)
        self.x.append("d")
        self.l.append(w2)
        z.display(0,w2)
    def mini(self):
        print("Mini statement:")
        if(self.x[-1]=="w"):
            print("The last transcarion is cashwithdrwal of",self.l[-1])
        else:
            print("the last transacation is deposit of",self.l[-1])
        if(self.x[-2]=="w"):
            print("The last second transcarion is cashwithdrwal of",self.l[-2])
        else:
            print("the last third transacation is deposit of",self.l[-2])
        if(self.x[-3]=="w"):
            print("The last third transcarion is cashwithdrwal of",self.l[-3])
        else:
            print("the last transacation is deposit of",self.l[-3])

    
    
        
    
    
        
        
        



    
    


