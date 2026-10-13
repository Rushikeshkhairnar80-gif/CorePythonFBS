import random 

correct_userid = "admin"
correct_password = "1234"

userid = input ("enter user id: ")
password = input ("enter passwoed: ")

if userid == correct_userid and password == correct_password:
    captcha = random.randint(1000, 9999)

    print("your captcha is:", captcha)

    user_captcha = int (input("enter captcha: "))

    if user_captcha == captcha:
        print("login successful")
    else:
        print("captcha failed")

else:
    print("invalid user id or password")