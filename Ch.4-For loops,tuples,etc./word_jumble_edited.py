# Ch.4 Challenge 3

# Edited word jumble game
# add the hints to a tuple with the same index as the corresponding word

# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import 2random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

# (edit) sequence of hints that is paired with each word (has same index as each word)
HINTS = ("an animal and a programming language",
         "one of the words in the title of this game",
         "the opposite of difficult",
         "the opposite of easy",
         "the response to a question",
         "the hardest instrument to spell")

# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# (edit) This loop is to determine the index of the randomly selected word
# so we can match it to the corresponding hint later in the program
count = 0
hint_count = 0

for i in WORDS:
    if i == word:
        break
    else:
        count += 1
    

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")

    # (edit) Asking the user if they want a hint is incorporated in the loop
    want_hint = input("Would you like a hint? y/n: ")
    if want_hint == "y":
        print("Hint: This word is", HINTS[count])
        guess = input("Your guess: ")
        hint_count += 1
    elif want_hint == "n":
        guess = input("Your guess: ")
    
if guess == correct and hint_count == 0:
    print("That's it!  You guessed it and you didn't even need a hint!\n")

elif guess == correct and hint_count > 0:
    print("Good job.. You guessed it, but you used a hint..\n")
    
print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
