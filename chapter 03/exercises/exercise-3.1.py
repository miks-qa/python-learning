# This program calculates the pay for an employee based on hours worked and hourly rate, including overtime pay for hours worked over 40.

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
if h > 40:
    pay = (40 * r) + ((h - 40) * (r *1.5))
else:
    pay = h * r
print(pay)