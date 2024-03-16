class showroom:
    def __init__(self):
        self.company_options = ["toyota", "mahendra", "mercedes"]
        self.model_options = {
            "toyota": ["camry", "glanza", "innova"],
            "mahendra": ["scorpio", "bolero", "xuv300"],
            "mercedes": ["eqs", "gle", "g"]
        }
        self.prices = {
            "toyota": {
                "camry": {"petrol": 520000, "diesel": 560000},
                "glanza": {"petrol": 580000, "diesel": 595000},
                "innova": {"petrol": 585000, "diesel": 599000}
            },
            "mahendra": {
                "scorpio": {"petrol": 625000, "diesel": 635000},
                "bolero": {"petrol": 630000, "diesel": 640000},
                "xuv300": {"petrol": 655000, "diesel": 665000}
            },
            "mercedes": {
                "eqs": {"petrol": 1155000, "diesel": 1185000},
                "gle": {"petrol": 1345000, "diesel": 1365000},
                "g": {"petrol": 1565000, "diesel": 1585000}
            }
        }
        self.c = 5 / 100
        self.s = 8 / 100
        self.ins = 20000
        self.c_n = None
        self.mod = None
        self.v = None

    def model(self):
        print("Welcome to the family!!")
        print("Choose your company:")
        for i in range(len(self.company_options)):
            print(str(i + 1) + ". " + self.company_options[i])
        while True:
            user_input = input("Enter your choice (number or text): ").strip().lower()
            if user_input.isdigit() and int(user_input) in range(1, len(self.company_options) + 1):
                self.c_n = self.company_options[int(user_input) - 1]
                break
            elif user_input in self.company_options:
                self.c_n = user_input
                break
            else:
                print("Invalid choice. Please try again.")
        print(f"Selected company: {self.c_n}")

        models = self.model_options[self.c_n]
        print("Choose model of your choice:")
        for i in range(len(models)):
            print(str(i + 1) + '. ' + models[i])
        while True:
            user_input = input("Enter your choice (number or text): ").strip().lower()
            if user_input.isdigit() and int(user_input) in range(1, len(models) + 1):
                self.mod = models[int(user_input) - 1]
                break
            elif user_input in models:
                self.mod = user_input
                break
            else:
                print("Invalid choice. Please try again.")
        print(f"Selected model: {self.mod}")

    def variant(self):
        while True:
            self.v = input("Choose petrol or diesel: ").strip().lower()
            if self.v in ['petrol', 'diesel']:
                break
            else:
                print("Invalid choice. Please choose 'petrol' or 'diesel'.")

    def display(self):
        if self.c_n in self.prices and self.mod in self.prices[self.c_n] and self.v in self.prices[self.c_n][self.mod]:
            x_showroomp = self.prices[self.c_n][self.mod][self.v]
            print("Showroom price is:", x_showroomp)
            on_road_price = x_showroomp + (self.c * x_showroomp) + (self.s * x_showroomp) + self.ins
            print("On road price is:", on_road_price)
        else:
            print("Invalid choice. Cannot calculate price.")


car = showroom()
car.model()
car.variant()
car.display()
