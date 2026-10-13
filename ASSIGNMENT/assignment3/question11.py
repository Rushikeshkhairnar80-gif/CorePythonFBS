# Ticket amount for 5 people

total = 0

for i in range (5):
    age = int (input("enter age: "))
    ticket = float(input("enter ticket amount: "))

    if age < 12:
        amount = ticket * 0.70
    elif age > 59:
        amount = ticket * 0.50
    else:
        amount = ticket

    total = total + amount

print("total ticket amount=", total)