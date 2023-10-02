# 100 Days of Code - Python
# Day 3
# Date :- 02/10/2023

# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# This is how you work out whether if a particular year is a leap year.

# on every year that is divisible by 4 with no remainder

# except every year that is evenly divisible by 100 with no remainder

# unless the year is also divisible by 400 with no remainder

year = int(input("Enter the year you want to check : "))

check1 = year%4
if check1 == 0 :
  check2 = year%100
  if check2 == 0 :
    check3 = year%400
    if check3 == 0 :
      print(f"{year} is a Leap year.")
    else :
      print(f"{year} is not a Leap year.")
  else : 
    print(f"{year} is a Leap year.")
else : 
  print(f"{year} is not a Leap year.")
