x = float (input("enter value of x: "))
n = int (input ("enter number of terms: "))

total = 0
sign = 1

for i in range(1, n + 1):
    term = (x ** i) / (2 * i - 1)
    total = (x ** i) / (2 * i - 1)
    sign = sign * -1

print("sum", total)