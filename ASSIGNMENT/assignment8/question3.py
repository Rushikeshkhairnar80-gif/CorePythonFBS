def series_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum
n = int (input("enter n: "))

print(" sum =", series_sum(n))