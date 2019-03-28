# Program that calculates the estimated hours and minutes for a trip

print("Travel Time Calculator")
print()

distance = int(input("Enter miles: "))
mph = int(input("Enter miles per hour: "))

travTime = distance / mph
hours = int(travTime)
minutes = int((travTime / 60) * 100)

print()
print("Estimated travel time")
print("Hours: ", hours)
print("Minutes: ", minutes)
