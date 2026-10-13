def digit_sum(num):
    sum = 0 

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    return sum 

n = int (input("enter number: "))

print("sum of digits =", digit_sum(n))
