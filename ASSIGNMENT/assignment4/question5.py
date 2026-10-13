#fibonacci series up to n

n = int (input("enternumber of terms: "))

a = 0
b = 1

for i  in range (n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c 