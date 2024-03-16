class showroom:
    def __init__(self):
        company_name = input("Choose your company you are interested in from Toyota, Mahindra, and Mercedes: ")
        self.c_n = company_name.capitalize()

    def model(self):
        print("Welcome to", self.c_n, "family")
        if self.c_n == "Toyota":
            m = input("Choose model of your choice from Camry, Glanza, and Innova: ")
            return m
        elif self.c_n == "Mahindra":
            m = input("Choose model of your choice from Scorpio, Bolero, XUV300: ")
            return m
        elif self.c_n == "Mercedes":
            m = input("Choose model of your choice from EQS, GLE, and G: ")
            return m

    def variant(self):
        var = input("Choose petrol or diesel: ")
        self.v = var
        print("You have selected", self.v, "variant.")

car = showroom()
selected_model = car.model()
car.variant()
