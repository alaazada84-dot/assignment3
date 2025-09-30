username = 1
passward = 1
n=1
while n<=3:
    username = input("Enter your username: ")
    passward = input("Enter your password: ")
    if username == "admin" and passward == "1234":
        print("Login successful!") 
        break
    else:
        n=n+1
else:
    print("Account locked")
