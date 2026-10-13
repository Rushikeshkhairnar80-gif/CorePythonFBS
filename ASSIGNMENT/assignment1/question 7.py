import math

a = float (input("Enter a: "))
b = float (input("Enter b:"))
c = float (input("Enter c: "))

D = b**2- 4*a*c

if D >0:
    root1 =(-b + math.sqrt(D)) / (2*a)
    root2 =(-b - math.sqrt(D)) / (2*a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif D== 0:
    root = -b / (2*a)
    print ("both root are =", root)
else:
    print("root are imaginary")