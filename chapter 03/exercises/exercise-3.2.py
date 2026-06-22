# This program prompts the user to enter a score and then converts that score into a letter grade based on a predefined grading scale. It also includes error handling to manage cases where the input is not a valid number between 0.0 and 1.0.

score = input("Enter Score:")
try:
    s = float(score)
except:
    s = -0.1
if s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s >= 0.0:
    print("F")
else:
    print("Invalid score")