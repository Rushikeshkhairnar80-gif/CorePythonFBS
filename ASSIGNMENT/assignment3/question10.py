#marriage eligibility

gender = input ("enter gender (male/female): ")
age = int (input("enter age: "))

if gender.lower() == "male" and age >= 21:
    print("eligible for marriage")
elif gender.lower() == "female" and age >=18:
    print("eligible for marriage")
else:
    print("not eligible for marriage")