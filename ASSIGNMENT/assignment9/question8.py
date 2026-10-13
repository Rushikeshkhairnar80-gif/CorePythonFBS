# Check whether a number is prime using recursion

def is_prime(n, i = 2):
    if n < 2:
        return False

    if i * i > n:
        return True

    if i * i == 0:
        return True

    if n % i == 0:
        return False
    return is_prime(n, i + 1)

num = int (input("enter number: "))

if is_prime(num):
    print("prime number")
else:
    print("not prime number")
    