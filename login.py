def login():
   
    while True:
        username= input("username:")
        password= input("password :")
        if username==password :
            print("login successful")
            break
        else:
            print("invalid credentials")
login()
