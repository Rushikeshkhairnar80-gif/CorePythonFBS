#numbers in a range divisible by a given number

start = int(input("enter starting number: "))
end = int(input("enter ending number: "))
num = int(input("enter divisor: "))

for i in range(start, end + 1):
    if i % num == 0:
        print(i)