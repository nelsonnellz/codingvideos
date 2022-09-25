

#### a number guessing game using python

## first import modules

import random

n = random.randrange(1, 10)

picked_number = int(input("Enter any number"))

while n != picked_number:
    if picked_number < n:
        print("Too low try a higher number: ")
        picked_number= int(input("Enter number again: "))

    elif picked_number > n:
        print("Too high try a lower number")
        picked_number=int(input("Enter number again"))

    else:
        break

print("Bingo!!!! You Guessed Right")
