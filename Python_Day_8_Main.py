# 100 Days of Code - Python
# Day 8
# Date :- 11/10/2023

# Project Title :- "Caesar Cipher"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

for letter in text :
    if letter in alphabet :
        position = alphabet.index(letter)
        if direction == "encode" :
            new_position = position + shift
            new_letter = alphabet[new_position]
            print(new_letter, end='')
        elif direction == "decode" :
            new_position = position - shift
            new_letter = alphabet[new_position]
            print(new_letter, end='')
    else :
        print(letter, end='')
