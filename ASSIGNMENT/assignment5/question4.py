start = int(input("enter starting number: "))
end = int (input("enter ending number: "))

for n in range(start, end + 1):

    temp = n 
    digits = 0

    while temp > 0:
        digits = digits + 1
        temp = temp // 10

    temp = n 
    total = 0

    while temp > 0:
        digit = temp  % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == n:
        print(n)