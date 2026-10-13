correct_userid = "admin"
correct_password = "1234"

userid = input ("enter user id: ")
password = input ("enter password: ")

if userid == correct_userid and password == correct_password:
    print ("login successful")
else:
    print("invalid user id or password")