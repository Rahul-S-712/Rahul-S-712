# 100 Days of Code - Python
# Day 3
# Date :- 02/10/2023

# Congratulations, you've got a job at Python Pizza!
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want ? S, M or L ? : ")
add_pepperoni = input("Do you want to add pepperoni ? Y or N ? : ")
extra_cheese = input("Do you want to add extra cheese ? Y or N ? : ")

bill = 0
if size == 'S' :
  bill = bill + 15
  if add_pepperoni == 'Y' :
    bill = bill + 2
  if extra_cheese == 'Y':
    bill = bill + 1
  print (f"Your final bill is: ${bill}.")
elif size == 'M' or 'L' :
  if size == 'M' :
    bill = bill + 20
  if size == 'L' :
    bill = bill + 25
  if add_pepperoni == 'Y' :
    bill = bill + 3
  if extra_cheese == 'Y' :
    bill = bill + 1
  print(f"Your final bill is: ${bill}.")
