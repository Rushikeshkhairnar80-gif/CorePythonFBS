n = int (input("enter n: "))

total = 0

for i in range(1, n + 1):
    total = total + n ** i

print("sum =", total)