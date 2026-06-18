#This program prompts the user to enter a temperature in Celsius and converts it to Kelvin and Fahrenheit.

c = input("Temperature in Celsius:")
kelvin = float(c) + 273.15
print("Temperature in Kelvin:", kelvin)
fahrenheit = float(c) * 9/5 + 32
print("Temperature in Fahrenheit:", fahrenheit)