# 3 Digit Number Palindrome

num = int(input("enter a 3 digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a == c:
    print("palindrome number")
else:
    print(" not a palindrome number")
    