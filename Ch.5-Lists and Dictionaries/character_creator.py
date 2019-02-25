# Ch.5: Challenge 2
# Character Creator

# player given a pool of 30 points
# can buy 4 attributes (strength, health, wisdom, dexterity)
# can sell attributes back to get his points points back

attributes = {
            "strength": 3,
            "health": 1,
            "wisdom": 4,
            "dexterity": 2
            }

my_player = {
            "strength": 0,
            "health": 0,
            "wisdom": 0,
            "dexterity": 0
            }

points = 30
choice = None

while choice != 0:

    print(
    """
    Character Creator
    
    0 - Quit
    1 - List Your Players Attributes and Points
    2 - Buy an Attribute
    3 - Sell an Attribute
    """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")
    
    # List my players attributes -----------------------------------------
    elif choice == "1":
        
        print("Points:", points)
        print(my_player)


    # Buy an attribute ---------------------------------------------------
    elif choice == "2":
        
        buy_attr = input("What attribute would you like to buy: ")

        # if what the user wants to buy is an item in the dictionary
        # and the user has enough points to buy that item 
        if attributes.get(buy_attr) and attributes[buy_attr] <= points:

        # add the value of that attribute towards the running total for
        # that attribute in the users dictionary
        # subtract the value of that attribute from points available
            my_player[buy_attr] += attributes[buy_attr]
            points -= attributes[buy_attr]

        # catches typing errors for user input of attribute name
        else:
            print("try again")


    # Sell an attribute --------------------------------------------------
    elif choice == "3":
        sell_attr = input("What attribute would you like to sell: ")

        # if user input is an attribute and the user actually has bought this attribute
        if sell_attr in my_player and my_player[sell_attr] > 0:

        # subtract the value of the this attribute from the users dictionary
        # add the value of that attribute back to the players avaiable points
            my_player[sell_attr] -= attributes[sell_attr]
            points += attributes.get(sell_attr)

        # catches typing errors for user input of attribute name
        else:
            print("try again")

