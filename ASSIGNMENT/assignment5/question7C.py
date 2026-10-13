n = int (input("enter number of terms: "))

total = 0 
term = 1

for i in range(1, n + 1):
    total = total + term
    term = term * 2

print("sum =", total)