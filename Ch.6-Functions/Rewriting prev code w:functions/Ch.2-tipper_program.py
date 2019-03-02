# Ch.2: Challenge 3
# Tipper Program

def intro():
    print("\nLet me calculate your tip for you..")

def user_bill():
    bill = float(input("Enter the total cost of your meal: $ "))
    return bill

def tip_calc(bill):
    fifteen = bill * .15
    twenty = bill * .2
    fifteen = round(fifteen, 2)
    twenty = round(twenty, 2)
    return fifteen, twenty

def tip_options(fifteen, twenty):
    print("\nA 15% tip is: $", fifteen)
    print("A 20% tip is: $", twenty)

def tip_choice():
    tip = int(input("\nWould you like to tip 15% or 20%? 15/20: "))
    return tip

def total(tip, bill, fifteen, twenty):
    if tip == 15:
        print("Okay cheapo your total is $ ", bill + fifteen,"\n")
    elif tip == 20:
        print("Thank you that's very generous.\
     Your total is $", bill + twenty,"\n")

def main():
    intro()
    bill = user_bill()
    fifteen, twenty = tip_calc(bill)
    tip_options(fifteen, twenty)
    tip = tip_choice()
    total(tip, bill, fifteen, twenty)

main()

