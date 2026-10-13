n = int (input("enter how many prime number: "))

count = 0
num = 2

while count < n:

    divisor_count = 0

    for i in range (1, num + 1):
        if num % i == 0:
            divisor_count = divisor_count + 1

    if divisor_count == 2:
        print(num)
        count = count + 1

    num = num + 1