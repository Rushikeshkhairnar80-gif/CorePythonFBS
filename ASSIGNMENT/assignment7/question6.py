n = 5 

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        if j == 1 or j == n - i + 1:
            print(i + j - 1, end=" ")
        else:
            print(" ", end="")
    
    print()