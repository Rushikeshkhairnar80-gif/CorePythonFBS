# Sum of series:

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def sum_series(n):
    if n == 0:
        return 0
    return fact (n) + sum_series(n - 1)

n = int (input("enter n: "))
print("sum =", sum_series(n))