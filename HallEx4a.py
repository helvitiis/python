choice = "y"

while choice.lower() == "y":

    print("Change Calculator")
    print()

    i = int(input("Enter number of cents (0-99): "))

    q = i//25
    if q == 0:
        print("No quarters")
    else:
        print("Quarters", q)
        i = i%25

    d = i//10
    if d == 0:
        print("No dimes")
    else:
        print("Dimes", d)
        i = i%10

    n = i//5
    if n == 0:
        print("No nickels")
    else:
        n = print("Nickles", n)
        i = i%5

    p = i//1
    if p == 0:
        print("No pennies")
    else:
        p = print("Pennies", p)

    print()
    choice = input("Continue? (y/n): ")
    print()

print("Bye!")
