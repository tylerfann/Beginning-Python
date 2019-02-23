# Ch.4 Challenge 4
# Word guessing game

# computer picks a random word and the player has to guess that word 
# computer says how many letters are in the word 
# player gets 5 chances to ask if letter in word 
# computer responds with yes or no 
# then player guesses the word 

# Import random module and store words and hints in tuples
import random

WORDS = ("chair", "book", "pillow", "window", "television")
HINTS = ("Something to sit on",
         "Used to learn and we all had them in school",
         "Something to rest your head on",
         "You wouldn't be able to see outside your house without these",
         "Also know as the 'boob' tube")

# Choose a random word from the WORDS tuple
word = random.choice(WORDS)

# Find the index for the randomly selected word, so it can be used to find
# the corresponding hint
index = 0

for i in WORDS:
    if i == word:
        break
    else:
        index += 1

# initialize the guess count, so the user on gets 5 total guesses 
guess_count = 1

# Welcome to the game, computer displays how many letters are in the
# random word and the corresponding hint
print("\t\t\tWelcome to the Word Guesser Game")
print("\nYour word has", len(word), "letters in it")
print("Here's a hint:", HINTS[index] + "\n")

# Loop allows the player to guess 5 times, if the players guess
# is in the random word then computer says yes if not computer says no
while guess_count <= 5:
    guess = input("Guess a letter: ")
    if guess in word:
        print("Yes, '" + guess.upper() + "' is in the word\n")
    else:
        print("No, '" + guess.upper() + "' is NOT in the word\n")
    guess_count += 1

# Computer prompts the playe to guess the full word and
# displays if he/she is correct or incorrect
print("That's all the hints you're getting!\n")
guess_word = input("Guess the full word: ")
if guess_word == word:
    print("Great job you guesssed it!\n")
else:
    print("Not quite.. The word was", word + "\n")





    
