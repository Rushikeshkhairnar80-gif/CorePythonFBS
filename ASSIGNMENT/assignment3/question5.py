a = int (input("enter first side:"))
b = int (input("enter second side:"))
c = int (input("enter third sidev:"))

if a == b and b == c:
    print("equilateral triangle")
elif a == b or b == c or a == c:
    print("isosceles triangle")
else:
    print("scalene triangle")