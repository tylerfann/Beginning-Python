# Ch.3: Challenge 2
# Coin Flipper

import random

def program_intro():
    print("Coin Flipper")
    print("Lets flip a coin 100 times and see the results\n")

def flip_coin(head_count, tail_count):
    coin = random.randint(1,2)
    
    if coin == 1:
        head_count += 1
    else:
        tail_count += 1
    return head_count, tail_count

def results(head_count, tail_count):
    print("Heads landed:", head_count,"times")
    print("Tails landed:", tail_count,"times")

def main():
    total = 0
    head_count = 0
    tail_count = 0
    
    program_intro()
    while total < 100:
        head_count, tail_count = flip_coin(head_count, tail_count)
        total += 1
    results(head_count, tail_count)

main()
    
        
        
    
