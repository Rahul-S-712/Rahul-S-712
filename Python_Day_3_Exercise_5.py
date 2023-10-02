# 100 Days of Code - Python
# Day 3
# Date :- 02/10/2023

# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."

from time import sleep
name1 = input("Enter the first name : ")
name2 = input("Enter the second name : ")
print("Please wait while the love calculator calculates your scores....")
sleep(5)

name = name1+name2
length = len(name)

i = 0
j = 0
true = 0
love = 0

while i < length :
  if name[i] == 't':
    true = true + 1
  elif name[i] == 'r':
    true = true + 1
  elif name[i] == 'u':
    true = true + 1
  elif name[i] == 'e':
    true = true + 1
  elif name[i] == 'T':
    true = true + 1
  elif name[i] == 'R':
    true = true + 1
  elif name[i] == 'U':
    true = true + 1
  elif name[i] == 'E':
    true = true + 1
  else :
    true = true
  i = i+1

while j < length :
  if name[j] == 'l':
    love = love + 1
  elif name[j] == 'o':
    love = love + 1
  elif name[j] == 'v':
    love = love + 1
  elif name[j] == 'e':
    love = love + 1
  elif name[j] == 'L':
    love = love + 1
  elif name[j] == 'O':
    love = love + 1
  elif name[j] == 'V':
    love = love + 1
  elif name[j] == 'E':
    love = love + 1
  else :
    love = love
  j = j+1

# print(true)
# print(love)

true_number = str(true)
love_number = str(love)

combined_number = true_number+love_number
number = int(combined_number)

if number < 10 or number > 90 :
  print(f"Your score is {number}, you go together like coke and mentos.")
elif number > 40 and number < 50 :
  print(f"Your score is {number}, you are alright together.")
else :
  print(f"Your score is {number}.")
