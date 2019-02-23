# Ch.3: Challenge 2
# Coin Flipper

import random

coin = ""
head_count = 0
tail_count = 0
total = 0

print("Coin Flipper")
print("Lets flip a coin 100 times and see the results\n")

while total < 100:
    coin = random.randint(1,2)
    if coin == 1:
        head_count += 1
    elif coin == 2:
        tail_count += 1
    total += 1

print("Heads landed", head_count)
print("Tails landed", tail_count)
