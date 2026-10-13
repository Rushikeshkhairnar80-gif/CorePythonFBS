m1 = int(input("enter marks of subject 1: "))
m2 = int(input("enter marks of subject 2: "))
m3 = int(input("enter marks of subject 3: "))
m4 = int(input("enter marks of subject 4: "))
m5 = int(input("enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("total =", total)
print("percentage =", percentage)

if percentage >= 75:
    print("distinction")

elif percentage >=60:
    print("first class")

elif percentage >=50:
    print("second class")

elif percentage >= 35:
    print("pass")

else:
    print("fail")