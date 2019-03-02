# Guess My Number (Reversed) edit for ch.6 challenge 2
#
# The user picks a random number between 1 and 100
# The computer tries to guess it and the user lets
# the computer know if the guess is too high, too low
# or right on the money

# Initialize Variables

low = 1
high = 100
tries = 7
guess = 50

# Display game instructions
def game_instructions():
    print("\nWelcome to 'Guess My Number Reversed!")
    print("Pick a number between 1 and 100 and the computer will try and guess it\n")
    
# Define ask_number function
def ask_number(low, high, tries):
    """Ask for a number within a range."""
    the_number = None
    while the_number not in range(low, high):
        the_number = int(input("Enter a number between 1-100: "))
    return the_number
    print("The computer has", tries, "tries to guess your number\n")

# How the computer can win
def computer_wins(tries, guess, the_number):
    """If computers guess equals the players number"""
    if guess == the_number and tries > 0:
        print("The computer guessed your number:", guess)
        print("It wins!")

# How the computer can loss
def computer_loses(tries, guess, the_number):
    if tries == 0 and guess != the_number:
        print("\nSorry computer you lose!")
        print("The humans number was", the_number)

# Computer guessing logic
def computer_guess(low, high, the_number):
    global tries
    guess = (low + high) // 2
    if guess > the_number:
        high = guess
    elif guess < the_number:
        low = guess + 1
    tries -= 1
    return guess, tries

# Prints the computers guess and amount of guess remaining
def display_guess(guess, tries):
    print("The computer guessed", guess, ". It has", tries, "guesses remaining")

# Main program
def main():
    game_instructions()
    the_number = ask_number(low, high, tries)
    global guess
    while guess != the_number:
        guess = computer_guess(low, high, the_number)
        display_guess(guess, tries)
        if computer_wins(tries, guess, the_number) is True:
            break
        elif computer_loses(tries, guess, the_number) is True:
            break

# Running the main program
main()
    
    
    
        
    

                 

