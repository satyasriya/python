Number = int(input("Please Enter any Number: "))
Sum = 0

while Number > 0:
    Reminder = Number % 10
    Sum += Reminder
    Number //= 10

print("\nSum of the digits of the given Number =",Sum)
