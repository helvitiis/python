# Create a program that calculates the tip and total for a meal.

print("This program will calculate the tip and total for your meal.")
cost = float(input("Please input the cost of your meal: "))
tipPer = int(input("Would you like to leave a 10%, 15%, or 20% tip? [Enter 10, 15, or 20.]: "))

tip = cost * (tipPer / 100)
total = cost + tip

tipFinal= round(tip, 2)
totalFinal= round(total, 2)

print("Cost of Meal: ", cost)
print("Tip percent: ", tipPer, "%")
print()
print("Tip amount: $", tipFinal)
print("Total amount: $", totalFinal)
