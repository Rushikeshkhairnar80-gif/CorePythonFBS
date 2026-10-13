# check armstrong number

n = int (input("enter anumber: "))

temp = n 
digits = 0

while temp > 0:
    digits = digits + 1
    temp = temp // 10

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if sum == n:
    print("armstrong number")
else:
    print("not an armstrong number")
