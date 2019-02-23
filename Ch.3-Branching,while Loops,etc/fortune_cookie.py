# Ch.3: Challenge 1
# Fortune Cookie simulation

import random

rand_fortune = ""
exit_program = ""
cookie1 = "\nThe early bird gets the worm, but the second mouse gets the cheese."
cookie2 = "\nBe on the alert to recognize your prime at whatever time of your life it may occur."
cookie3 = "\nYour road to glory will be rocky, but fulfilling."
cookie4 = "\nCourage is not simply one of the virtues, but the form of every virtue at the testing point."
cookie5 = "\nPatience is your alley at the moment. Don’t worry!"

print("Fortune Cookie Simulation")
input("Press enter to recieve a random fortune")


while True:
    rand_fortune = random.randint(1,5)
    if rand_fortune == 1:
        print(cookie1)
    elif rand_fortune == 2:
        print(cookie2)
    elif rand_fortune == 3:
        print(cookie3)
    elif rand_fortune == 4:
        print(cookie4)
    elif rand_fortune == 5:
        print(cookie5)
    exit_program = input("\nType 'q' to quit or press enter for another fortune\n")
    if exit_program == "q":
        print("Goodbye!")
        break
        
