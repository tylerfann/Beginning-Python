# Ch.2: Challenge 4
# Car Salesman Program (Edit for Ch.6, adding functions)

# Program Intro
def intro():
    print("\nCongrats on the new car!\n\
     Lets crunch the numbers..")

# User enters new cars base cost
def base_cost():
    base = int(input("\nEnter the base price of your new car: $ " ))
    return base

# Calculate fees
def calc_fees(base):
    tax_fee = base * .15
    license_fee = base * .05
    dealer_prep = 200
    delivery = 400
    return tax_fee, license_fee, dealer_prep, delivery

def calc_total(base, tax_fee, license_fee, dealer_prep, delivery):
    total = base + tax_fee + license_fee + dealer_prep + delivery
    return total

def display_costs(total, base, tax_fee, license_fee, dealer_prep, delivery):
    print("\nYour all inclusive price is: $ ", total)
    print("\nHere's the cost breakdown: ")
    print("\nBase: $", base, "\n\
    Tax: $", tax_fee, "\n\
    License fee: $", license_fee, "\n\
    Dealer Prep: $", dealer_prep, "\n\
    Destination fee: $", delivery, "\n\
    Total Cost: $", total,"\n")

def main():
    intro()
    base = base_cost()
    tax_fee, license_fee, dealer_prep, delivery = calc_fees(base)
    total = calc_total(base, tax_fee, license_fee, dealer_prep, delivery)
    display_costs(total, base, tax_fee, license_fee, dealer_prep, delivery)

main()
    
    
