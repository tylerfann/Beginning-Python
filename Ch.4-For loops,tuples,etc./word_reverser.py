# Ch.4: Challenge 2
# Backward message printer
# user enters a string and computer prints it out backwards


# user enter word(s)

word = input("Enter a word: ")

# initialize variables for new word, indexing variable and counter
new_word = ""
end = len(word) - 1
count = 0

# start loop, program runs until the length of the users word
# is the same length as the new word

while len(new_word) < len(word):

# targeting the last letter in users word through the end variable
# if that letter is already in new word subtract count from end and
# add that letter

    if word[end] in new_word:
        new_word += word[end - count]
        
# if the last letter isnt't in the new word add it to new word
    else:
        new_word += word[end]
        
# add one to the count variable each loop

    count += 1

# after while loop conditional isn't true print the new word

print("Here is that word backwards:", new_word)
