a = int (input("Enter first side:"))
b = int (input("enter second side:"))
c = int (input("enter third side:"))

if a + b > c and a + c > b and b and b+ c > a:
    print("valid triangle")
else:
    print("invalid triangle")