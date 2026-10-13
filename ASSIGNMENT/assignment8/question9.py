# Check palindrome number

def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev 

def is_palindrome(num):
    return num == reverse_number(num)

n = int(input("enter number: "))

if is_palindrome(n):
    print("palindrome number")
else:
    print("not a palindrome number")