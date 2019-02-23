# Guess My Number (Reversed)
#
# The user picks a random number between 1 and 100
# The computer tries to guess it and the user lets
# the computer know if the guess is too high, too low
# or right on the money

import random  

print("\nWelcome to 'Guess My Number Reversed'!")
print("Pick a number between 1 and 100 and the computer will try and guess it\n")

# Initialize Variables

low = 1
high = 100
guess = 50
tries = 5

# Start Game

the_number = int(input("Enter a number between 1-100: "))
print("The computer has", tries, "tries to guess your number\n")

while guess != the_number:

    guess = (low + high) // 2
    if guess > the_number:
        high = guess
    elif guess < the_number:
        low = guess + 1
    tries -= 1
    if tries <= -1 and guess != the_number:
        print("Sorry computer you lose!\n")
        break

    print("The computer guessed", guess, ". It has", tries, "guesses remaining")

    if guess > the_number:
        print("The humans number is lower\n")
    elif guess < the_number:
        print("The humans number is higher\n")
    
                 
        
    

                 

