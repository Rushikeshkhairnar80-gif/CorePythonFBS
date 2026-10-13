def factorial (n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def factorial_series(n):
    sum = 0 
    for i in range(1, n + 1):
        sum = sum + factorial(i)
    return sum

n = int (input("enter n: "))

print("sum =", factorial_series(n))