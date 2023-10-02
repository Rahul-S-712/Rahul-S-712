# 100 Days of Code - Python
# Day 3
# Date :- 02/10/2023

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("Enter your height in meters.\nEg :- 1.55\nHeight ? "))
weight = int(input("Enter your weight in kilograms.\nEg :- 65\nWeight ? "))

BMI = round((weight/(height ** 2)),2)

if BMI < 18.5 :
  print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5 <= BMI < 25 :
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI < 30 :
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 30 <= BMI < 35 : 
  print(f"Your BMI is {BMI}, you are obese.")
elif BMI >= 35 :
  print(f"Your BMI is {BMI}, you are clinically obese.")
