# Ch.5 Challenge 1
# Program prints list of words in random order
# program prints all words and doesn't repeat any words

# imports
import random

# List with original order
WORDS = ["desk", "monitor", "coffee", "lamp", "printer",
         "macbook", "keyboard", "calander", "photos", "phone"]

# Initialize new list
new_list = []

# Loop that runs until the original list is empty
while WORDS:

    # Generates a random number between 0 and the length of the list
    # Random number is used as an index to choose an item from the list
    # and add it to the new list
    # Then that list item is removed from the original list so it is
    # not repeated 
    index = random.randrange(0, len(WORDS))
    new_list.append(WORDS[index])
    del WORDS[index]

# Display the new randomly ordered list
print(new_list)





