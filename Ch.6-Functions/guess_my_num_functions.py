# Guess My Number (Reversed) edited using functions
#
# The user picks a random number between 1 and 100
# The computer tries to guess it and the user lets
# the computer know if the guess is too high, too low
# or right on the money

# Game Introduction
def intro():
    print("\nWelcome to 'Guess My Number Reversed'!")
    print("Pick a number between 1 and 100 and the computer will try and guess it\n")
    
# Player enters his/her number
def get_num(tries):
    the_number = int(input("Enter a number between 1-100: "))
    print("The computer has", tries, "tries to guess your number\n")
    return the_number

# The computers guessing logic
def comp_guess(low, high, the_number, tries):
    guess = (low + high) // 2
    if guess > the_number:
        high = guess
    elif guess < the_number:
        low = guess + 1
    tries -= 1
    
    return low, high, guess, tries

# How the computer can win
def comp_wins(guess, the_number, tries):
    if guess == the_number and tries >= 0:
        print("The computer wins!\n")

# How the computer can lose
def comp_losses(guess, the_number, tries):
    if guess != the_number and tries == 0:
        print("Sorry computer you lose!\n")

# Displays the computers guess and guesses remaining
def display_guess(guess, tries):
    print("The computer guessed", guess, ". It has", tries, "guesses remaining")

# Main program
def main():
    low = 1
    high = 100
    guess = 50
    tries = 8
    
    intro()
    the_number = get_num(tries)
    comp_wins(guess, the_number, tries)
    comp_losses(guess, the_number, tries)
    
    while the_number != guess and tries > 0:
        low, high, guess, tries = comp_guess(low, high, the_number, tries)
        display_guess(guess, tries)
        comp_wins(guess, the_number, tries)
        comp_losses(guess, the_number, tries)

# Running the program    
main()    
                 
        
    

                 

