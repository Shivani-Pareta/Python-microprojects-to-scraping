#Check if a user's password meets basic safety criteria (at least 6 characters long and contains an exclamation mark !)

print("-----the quick password validator-----")

password = input("please enter a password : ")

if len(password)>=6 and "!" in password:
    print("strong password! Password accepted")
elif len(password)>=6:
    print("Moderate, but do not forget to include an ! mark")
else:
    print("Weak password! Must be at least 6 characters long and contain an ! mark")
