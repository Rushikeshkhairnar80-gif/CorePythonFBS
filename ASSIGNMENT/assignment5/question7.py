# solve the following series

n = int(input("enter n: "))

fact = 1 
total = 0

for i in range(1, n + 1):
    fact = fact * i
    total = total + fact

print ("sum =", total)