#!/usr/bin/env python3 # if you are using linux uncomment this line

# Cleaning the text 
phrase = input(f"\nInsert phrase --> ")
phrase = phrase.lower().strip()

def cesar_shift(text, shift): 
    result = ' '
    
    for char in text:
        if char.isalpha(): # if char.(a-z,A-Z==true)
            # chr(65)='A', ord('A')=65
    	    # % limits the loop to 26 and sums
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
            
    return result

loops = int(input("How many loops do you want: "))

for i in range(loops):
    print(f"Shift {i} -->' {cesar_shift(phrase, i)} '") #function call and loop
