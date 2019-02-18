# Ch.2: Challenge 3
# Tipper Program

print("\nLet me calculate your tip for you..")
bill = float(input("Enter the total cost of your meal: $ "))
fifteen_percent = bill * .15
twenty_percent = bill * .2

fifteen_percent = round(fifteen_percent, 2)
twenty_percent = round(twenty_percent, 2)

print("\nA 15% tip is: $", fifteen_percent)
print("A 20% tip is: $", twenty_percent)

tip = int(input("\nWould you like to tip 15% or 20%? 15/20: "))

if tip == 15:
    print("Okay cheapo your total is $ ", bill + fifteen_percent,"\n")
elif tip == 20:
    print("Thank you that's very generous.\
 Your total is $", bill + twenty_percent,"\n")

