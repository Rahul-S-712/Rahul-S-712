# 100 Days of Code - Python
# Day 2
# Date :- 01/10/2023

# Create a program using maths and f-Strings that tells us how many weeks we have left, 
# if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

age = input("Enter your age :\n")

number_of_weeks_in_a_year = 52
number_of_years_left_to_live = 90 - int(age)

number_of_weeks_left = number_of_weeks_in_a_year * number_of_years_left_to_live
weeks_left = round(number_of_weeks_left)

print(f"You have {weeks_left} weeks left.")
