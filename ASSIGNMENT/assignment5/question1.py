correct_userid = "admin"
correct_userid = "1234"

for i in range(3):
    userid = input("enter user id: ")
    password = input("enter password: ")

    if userid == correct_userid and password == correct_userid:
        print("login successful")
        break
    else:
        print("invalid user id or password")

else:
    print("3 attempts completed. program terminated.")