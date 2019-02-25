# Ch.5 Challenge 3
# Who's your daddy?

# program lets user enter name of male and produces name of father
# user can add, replace and delete son father pairs

family = {}

choice = None

while choice != 0:

    print(
    """
    Who's Your Daddy?
    
    0 - Quit
    1 - List Father/Son Duos
    2 - Create a Father/Son Duo
    3 - Replace a Father/Son Duo
    4 - Delete a Father/Son Duo
    """
    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye")
        break

    # List Items in dictionary
    elif choice == "1":
        if not family:
            print("There are no duos to display..")
            print("Create a new duo!")
        else:
            print("CHILD\tFATHER\n")
            for child in family:
                print(child.title() + "\t" + family[child].title())
            print()
            
    # add father/son pair
    elif choice == "2":
        son = input("What is the sons/daughters name: ")
        if son not in family:
            father = input("What is his/her fathers name: ")
            family[son] = father
        else:
            print("That duo is already listed")
        print()

    # replace father/son pair
    elif choice == "3":
        if not family:
            print("There are no duos to replace..")
            print("Create a new duo!")
        else:
            replace = input("Enter the name of the child to replace a duo: ")
            if replace in family:
                del family[replace]
                replace_key = input("What is the NEW sons/daughters name: ")
                replace_value = input("Whats the name of his/her father? ")
                family[replace_key] = replace_value
            else:
                print("That's not a key in the dictionary")
        print()

    # delete father/son pair
    elif choice == "4":
        if not family:
            print("There are no duos to delete..")
            print("Create a new duo!")
        else:
            delete = input("What duo would you like to delete: ")
            if delete in family:
                del family[delete]
            else:
                print("That's not a key in the dictionary")
        print()



