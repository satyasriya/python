class showroom:
    def __init__(self):
        self.company_options = {
            "1": "toyota",
            "2": "mahendra",
            "3": "mercedes"
        }
        self.model_options = {
            "toyota": ["camry", "glanza", "innova"],
            "mahendra": ["scorpio", "bolero", "xuv300"],
            "mercedes": ["eqs", "gle", "g"]
        }
        self.c_n = None
        self.c = 5/100  
        self.s = 8/100
        self.ins = 20000
        self.mod = ""

    def choose_option(self, options):
        while True:
            print("Choose one of the following options:")
            for num, choice in options.items():
                print(f"{num}. {choice}")
            user_input = input("Enter your choice (number or text): ").strip().lower()
            if user_input in options.values():
                return user_input
            elif user_input in options:
                return options[user_input]
            else:
                print("Invalid choice. Please try again.")

    def model(self):
        print("Welcome to the family!!")
        print("Choose your company:")
        self.c_n = self.choose_option(self.company_options)
        print(f"Selected company: {self.c_n}")
        
        models = self.model_options[self.c_n]
        print("Choose model of your choice:")
        self.mod = self.choose_option({str(i+1): model for i, model in enumerate(models)})
        print(f"Selected model: {self.mod}")

    def variant(self):
        while True:
            self.v = input("Choose petrol or diesel: ").strip().lower()
            if self.v in ['petrol', 'diesel']:
                break
            else:
                print("Invalid choice. Please choose 'petrol' or 'diesel'.")

    def display(self):
        x_showroomp = self.get_showroom_price()
        if x_showroomp is not None:
            print("Showroom price is:", x_showroomp)
            on_road_price = x_showroomp + (self.c * x_showroomp) + (self.s * x_showroomp) + self.ins
            print("On road price is:", on_road_price)
        else:
            print("Invalid choice. Cannot calculate price.")

    def get_showroom_price(self):
        if self.c_n == "toyota":
            if self.mod == "camry":
                if self.v == "petrol":
                    return 520000
                elif self.v == "diesel":
                    return 560000
            elif self.mod == "glanza":
                if self.v == "petrol":
                    return 580000
                elif self.v == "diesel":
                    return 595000
            elif self.mod == "innova":
                if self.v == "petrol":
                    return 585000
                elif self.v == "diesel":
                    return 599000
        elif self.c_n == "mahendra":
            if self.mod == "scorpio":
                if self.v == "petrol":
                    return 625000
                elif self.v == "diesel":
                    return 635000
            elif self.mod == "bolero":
                if self.v == "petrol":
                    return 630000
                elif self.v == "diesel":
                    return 640000
            elif self.mod == "xuv300":
                if self.v == "petrol":
                    return 655000
                elif self.v == "diesel":
                    return 665000
        elif self.c_n == "mercedes":
            if self.mod == "eqs":
                if self.v == "petrol":
                    return 1155000
                elif self.v == "diesel":
                    return 1185000
            elif self.mod == "gle":
                if self.v == "petrol":
                    return 1345000
                elif self.v == "diesel":
                    return 1365000
            elif self.mod == "g":
                if self.v == "petrol":
                    return 1565000
                elif self.v == "diesel":
                    return 1585000
        return None

car = showroom()
car.model()
car.variant()
car.display()
