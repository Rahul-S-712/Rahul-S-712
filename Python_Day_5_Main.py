# 100 Days of Code - Python
# Day 5
# Date :- 04/10/2023

# Project Title :- "Password Generator"

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

d = []
e = []
f = []

i = 0
j = 0
k = 0

while (i<=nr_letters-1) :
  a = random.randint(0,51)
  d.append(letters[a])
  i = i+1
  
while (j<=nr_numbers-1) :
  b = random.randint(0,9)
  e.append(numbers[b])
  j = j+1

while (k<=nr_symbols-1) :
  c = random.randint(0,8)
  f.append(symbols[c])
  k = k+1

net_list = []
l=0
m=0
n=0

while (l<=nr_letters-1) :
  net_list.append(d[l])
  l=l+1

while (m<=nr_numbers-1) :
  net_list.append(e[m])
  m=m+1

while (n<=nr_symbols-1) :
  net_list.append(f[n])
  n=n+1

random.shuffle(net_list)
print("Your new password could be - ",end="")
for character in net_list :
  print(character,end="")
