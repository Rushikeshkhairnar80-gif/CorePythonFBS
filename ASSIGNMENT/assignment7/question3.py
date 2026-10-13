n = 5 

for i in range (1, n + 1):
    print(1, end=" ")
    if i > 1:
        print(" " * (2 * i - 3), i, end="")
    print()