passengers = int(input("enter number of passengers: "))
ticket = float(input("enter ticket cost: "))

total = 0

for i in range (1, passengers + 1):
    age = int(input("enter age of passenger: "))

    if age < 12:
        amount = ticket * 0.70
    elif age > 59:
        amount = ticket * 0.50
    else:
        amount =ticket

    total = total + amount

print("total ticket amount=", total)