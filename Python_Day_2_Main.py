# 100 Days of Code - Python
# Day 2
# Date :- 01/10/2023

# Project Title :- "Bill Splitter with Tip Calculator In-Built"

print("Welcome to the Bill Splitter.\n")
bill = input("How much was the total bill ? $")
tip = input("\nWhat percentage tip would you like to give?\n7%, 10%, 12%, or 15%?\n(Enter only the number) : ")
ppl = input("\nHow many people to split the bill between ? ")

bill = float(bill)
tip = int(tip)
ppl = int (ppl)

split_amount = bill/ppl
tip_amount = ((tip/100)*bill)
final_split_amount = (split_amount + (tip_amount/ppl))
split = round(final_split_amount,2)

print(f"\nEach person should pay ${split}")
