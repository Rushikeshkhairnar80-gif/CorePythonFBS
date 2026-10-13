# sum 1 + 2 + 3 + ... + n 

def power_series (n):
    sum = 0 
    for i in range(1, n + 1):
        sum = sum + i ** i
    return sum

n = int (input("enter n: "))

print("sum =", power_series(n))
