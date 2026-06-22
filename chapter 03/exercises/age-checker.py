#This program checks if the user is a minor or an adult based on their age input. It also handles invalid inputs and negative ages.

age = input("Enter your age: ")
try:
    age = int(age)
    if age <= 0:
        print("Age cannot be zero or negative. Please enter a valid age.")
    elif age < 18:
        print("You are a minor.")
    elif age >= 18:
        print("You are an adult.")
    else:
        print("Invalid age entered.")
except:
    print("Invalid input. Please enter a whole number.")