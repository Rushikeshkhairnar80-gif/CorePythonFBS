feet = int(input("Enter feet: "))
inch = float(input("Enter inches: "))

total_inches = (feet * 12) + inch
total_cm = total_inches * 2.54
meter = total_cm / 100

print("meter =", meter)
print("centimeter =", total_cm)