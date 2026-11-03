print("-----Welcome to the safe age verifier------")

while True:
    try:
        user_name = input("Please enter your name:")
        user_age = int(input("Please enter your age:"))

        print(f"\n hi {user_name} you are {user_age}")

        if user_age >=18:
            print("Access Granted: You are an adult.")
        else:
            print("Access Denied: Minor account.")
        break

    except ValueError:
        print("XXXX Invalid Input! Please enter a valid output")

#the code runs without running into any problems coz of the try and except block that already tells the system how to handle the exceptions that could be encountered.

