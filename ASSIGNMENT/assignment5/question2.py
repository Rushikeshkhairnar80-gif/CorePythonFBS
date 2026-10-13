n = int (input("enter number of student: "))

total_percentage = 0 

for i in range(1, n + 1):
    print("student", i)

    m1 = float(input("enter subject 1 marks: "))
    m2 = float(input("enter subject 2 marks: "))
    m3 = float(input("enter subject 3 marks: "))
    m4 = float(input("enter subject 4 marks: "))
    m5 = float(input("enter subject 5 marks: "))

    percentage = (m1 + m2 + m3 + m4 + m5) / 5

    print("percentage =", percentage)

    total_percentage =total_percentage + percentage

average = total_percentage / n 

print("average percentage =", average)