# This is a simple calculator program that performs basic arithmetic operations: addition, subtraction, multiplication, and division. The user is prompted to enter two numbers and an operation, and the program outputs the result of the operation.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    else:
        return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(add(a, b))
elif operation == "-":
    print(subtract(a, b))
elif operation == "*":
    print(multiply(a, b))
elif operation == "/":
    print(divide(a, b))
else:
    print("Invalid operation.")