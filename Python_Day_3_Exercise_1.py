# 100 Days of Code - Python
# Day 3
# Date :- 02/10/2023

# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.

number = int(input("Enter the number you want to check : "))
remainder = number%2

if remainder == 0 :
  print(f"{number} is an even number")
else :
  print(f"{number} is an odd number")
