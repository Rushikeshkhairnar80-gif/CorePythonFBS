a = float(input("enter value of a: "))

total = 0 

for i in range (1, 11):
    total = total +(a ** i) / i

    print("s =", total)