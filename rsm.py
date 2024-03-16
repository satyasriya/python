import csv
class register:
    def registration(self,username,password,phno,email,city):
        self.uname = username
        self.pwd = password
        self.pno = phno 
        self.mail = email 
        self.city = city

        with open('register.csv','a',newline='') as file:
            s = csv.writer(file)
            s.writerow([self.uname,self.pwd,self.pno,self.mail,self.city])
    def login(self,username,password):
        with open('register.csv','r',newline='') as file:
            read = csv.DictReader(file)
            for row in read:
                if row['uname']==username and row['pow'] == password:
                    return True
        return False