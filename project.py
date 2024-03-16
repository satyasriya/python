class showroom:
    def __init__(self):
        company_name =input("Choose your company you are intrested from toyota,mahendra and mercedes:")
        self.c_n= company_name
        cgst = 5/100
        self.c = cgst
        sgst = 8/100
        self.s = sgst
        insurance = 20000
        self.ins = insurance
        self.mod=""
    def model(self):
        print("Welcome to ", self.c_n, "family!!")
        if self.c_n == "toyota":
            m=input("choose model of your choice from camry glanza and innova :")
            self.mod = m
            return m
        elif self.c_n == "mahendra":
            m=input("choose model of your choice from scorpio bolero xuv300 :")
            self.mod = m
            return m
        elif self.c_n == "mercedes":
            m=input("choose model of your choice from eqs gle and g :")
            self.mod = m
            return m
    def variant(self):
        var = input("choose petrol or disel:")
        self.v = var
    def display(self):
        if self.c_n=="toyota" and self.mod == "camry" and self.v == "petrol":
            x_showroomp = 520000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="toyota" and self.mod == "camry" and self.v == "disel":
            x_showroomp = 560000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="toyota" and self.mod == "glanza" and self.v == "petrol":
            x_showroomp = 580000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="toyota" and self.mod == "glanza" and self.v == "disel":
            x_showroomp = 595000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="toyota" and self.mod == "innova" and self.v == "petrol":
            x_showroomp = 585000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="toyota" and self.mod == "innova" and self.v == "disel":
            x_showroomp = 599000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mahendra" and self.mod == "scorpio" and self.v == "petrol":
            x_showroomp = 625000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mahendra" and self.mod == "scorpio" and self.v == "disel":
            x_showroomp = 635000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mahendra" and self.mod == "bolero" and self.v == "petrol":
            x_showroomp = 630000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mahendra" and self.mod == "bolero" and self.v == "disel":
            x_showroomp = 640000
            print(x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mahendra" and self.mod == "xuv300" and self.v == "petrol":
            x_showroomp = 655000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mahendra" and self.mod == "xuv300" and self.v == "disel":
            x_showroomp = 665000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mercedes" and self.mod == "eqs" and self.v == "petrol":
            x_showroomp = 1155000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mercedes" and self.mod == "eqs" and self.v == "disel":
            x_showroomp = 1185000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mercedes" and self.mod == "gle" and self.v == "petrol":
            x_showroomp = 1345000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mercedes" and self.mod == "gle" and self.v == "disel":
            x_showroomp = 1365000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mercedes" and self.mod == "g" and self.v == "petrol":
            x_showroomp = 1565000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        elif self.c_n=="mercedes" and self.mod == "g" and self.v == "disel":
            x_showroomp = 1585000
            print("showroom price is: ",x_showroomp)
            on_road_price = x_showroomp + (self.c*x_showroomp) +(self.s*x_showroomp) +self.ins
            print("on road price is: ",on_road_price)
        else:
            print("invalid")
car = showroom()
car.model()
car.variant()
car.display()
        
        
                
            
