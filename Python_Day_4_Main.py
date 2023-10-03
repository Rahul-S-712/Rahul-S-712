# 100 Days of Code - Python
# Day 4
# Date :- 03/10/2023

# Project Title :- "Rock-Paper-Scissor Game versus the Computer"

import random

a = int(input("What do you choose ? Enter '0' for Rock, '1' for Paper, and '2' for Scissors.\nYour choice : "))
if a == 0 :
  print("\nYou chose Rock.")
elif a == 1 :
  print("\nYou chose Paper.")
elif a == 2 :
  print("\nYou choose Scissors.")
else :
  print("\nInvalid choice.")
  quit()

b = random.randint(0,2)

if b == 0 :
  print("\nThe computer chose Rock.")
elif b == 1 :
  print("\nYou computer chose Paper.")
elif b == 2 :
  print("\nYou computer chose Scissors.")

if ((a==0 and b==0)or(a==1 and b==1)or(a==2 and b==2)) :
  print("\nThe game is a Draw.")
elif((a==0 and b==1)or(a==1 and b==2)or(a==2 and b==0)) :
  print("\nThe computer wins.")
elif((b==0 and a==1)or(b==1 and a==2)or(b==2 and a==0)) :
  print("\nYou are the winner.")
