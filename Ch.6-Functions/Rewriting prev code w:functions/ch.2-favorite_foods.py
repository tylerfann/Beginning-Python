#Ch.2: Challenge 2
# Favorite foods program

def fav_food():
    fav_food1 = input("Enter your favorite food: ")
    fav_food2 = input("Enter your second favorite food: ")

    combined = fav_food1 + fav_food2

    print("\nYour favorite foods combined equals", combined.replace(" ", ""))

fav_food()
