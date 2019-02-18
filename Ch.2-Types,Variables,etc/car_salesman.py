# Ch.2: Challenge 4
# Car Salesman Program

print("\nCongrats on the new car!\
 Lets crunch the numbers..")

base = int(input("\nEnter the base price of your new car: $ " ))

# Fees

tax_fee = base * .15
license_fee = base * .05
dealer_prep_fee = 200
delivery_fee = 400

total_price = base + tax_fee + license_fee + dealer_prep_fee + delivery_fee

print("\nYour all inclusive price is: $ ", total_price)
print("\nHere's the cost breakdown: ")
print("\nBase: $", base, "\n\
Tax: $", tax_fee, "\n\
License fee: $", license_fee, "\n\
Dealer Prep: $", dealer_prep_fee, "\n\
Destination fee: $", delivery_fee, "\n\
Total Cost: $", total_price,"\n")
