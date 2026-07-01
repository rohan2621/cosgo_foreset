print("Login system")
user_name=input("Enter your username: ")
password=input("Enter your pass: ")

while True:
    pass_input=input("Enter your password to login :")
    if pass_input==password:
        print("login successful")
        break;
    else:
        print("Password incorrect")
        pass
