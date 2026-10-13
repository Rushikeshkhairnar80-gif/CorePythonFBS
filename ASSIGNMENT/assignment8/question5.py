# Sum of all prime numbers between 1 to n

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def prime_sum(n):
    sum= 0

    for i in range(1, n + 1):
        if is_prime(i):
            sum = sum + i


    return sum

n = int(input("enter n: "))

print("sum of prime numbers =", prime_sum(n))