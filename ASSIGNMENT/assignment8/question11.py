def is_armostrong(num):
    original = num
    digits = len (str(num))
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10

    return sum == original

n = int (input("enter number: "))

if is_armostrong(n):
    print("armstrong number")
else:
    print("not an armstrong number")