# This program simulates a simple login system where the user is prompted to enter a username and password. It checks if the credentials match predefined values and provides appropriate feedback.

username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "admin123":
        print("Login successful! Welcome, Admin.")
    else:
        print("Invalid username or password.")
else:
    print("Invalid username or password.")