# 100 Days of Code - Python
# Day 4
# Date :- 03/10/2023

# You are going to write a program that will mark a spot on a map with an X.
# When map is printed this is what it looks like, notice the nesting:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. 
# So we've used this line of code print(f"{row1}\n{row2}\n{row3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# Your job is to write a program that allows you to mark a square on the map using a letter-number system.

# First, your program must take the user input and convert it to a usable format.

# Next, you need to use that input to update your nested list with an "X".

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.\n")
position = input("Where do you want to put the treasure ?\nType A,B, or C for longitudes and 1,2,3 for latitudes.\nEg:- 'A2' or 'C1'\nEnter your coordinates : ")

if position == "A1" : 
  line1.insert(0,"X")
  line1.pop(1)
elif position == "B1" :
  line1.insert(1,"X")
  line1.pop(2)
elif position == "C1" :
  line1.insert(2,"X")
  line1.pop(3)
elif position == "A2" :
  line2.insert(0,"X")
  line2.pop(1)
elif position == "B2" :
  line2.insert(1,"X")
  line2.pop(2)
elif position == "C2" :
  line2.insert(2,"X")
  line2.pop(3)
elif position == "A3" :
  line3.insert(0,"X")
  line3.pop(1)
elif position == "B3" :
  line3.insert(1,"X")
  line3.pop(2)
elif position == "C3" :
  line3.insert(2,"X")
  line3.pop(3)

print(f"{line1}\n{line2}\n{line3}")
