def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def armstrong(n, digits, original):
    if n == 0:
        return 0

    digit = n % 10
    return digit ** digits + armstrong(n // 10, digits, original)

num = int (input("enter number: "))

digits = count_digits(num)

if armstrong(num, digits, num) == num:
    print("armstrong number")
else:
    print("not armstrong number")