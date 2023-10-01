# Day 2
# Date :- 01/10/2023

# Write a program that calculates the Body Mass Index (BMI) 
# from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. 
# e.g. If a tall person and a short person both weigh the same amount, 
# the short person is usually more overweight.

# The BMI is calculated by dividing 
# a person's weight (in kg) by the square of their height (in m)

height = input("Enter height in meters (eg :- 1.65) :-\n")
weight = input("Enter weight in kilograms (eg :- 75) :-\n")

w = float(weight)
h = float(height)

bmi = (w/(h ** 2))
bmi_value = int(bmi)
bmi_string = str(bmi_value)
print("\nYour BMI is " + bmi_string)
