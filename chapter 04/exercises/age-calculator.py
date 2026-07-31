# This is a simple age calculator program that calculates the current age based on the birth year and current year provided by the user. The program includes input validation to ensure that the years entered are valid and logical. It also has try-except blocks from previous chapters to handle invalid input.

def current_age(birth_year, current_year):
    return current_year - birth_year

try:
    birth_year = int(input("Enter birth year: "))
    current_year = int(input("Enter current year: "))

    if birth_year > current_year:
        print("Birth year cannot be greater than current year.")
    elif birth_year < 1800:
        print("Birth year must be greater than or equal to 1800.")
    elif current_year < 1800:
        print("Current year must be greater than or equal to 1800.")
    else:
        age = current_age(birth_year, current_year)
        print("Age:", age)

except:
    print("Invalid input. Please enter valid years.")