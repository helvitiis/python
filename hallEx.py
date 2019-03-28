import csv

# a file in the current directory
FILENAME = "monthly_sales.csv"

def write_items(items): # writing items
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(items)   

def read_item(): # reading items
    items = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            items.append(row)
    return items

def monthly_list(items): # defining variable for the monthly list
    for i in range(len(items)):
        item = items[i]
        print(item[0] + " - " + item[1]) # strings output together
    print()

def yearly_item(items): # defining yearly items function
    for i in range(len(items)):
        item = items[i]
        yearly_total = sum(item[1])
        monthly_average = yearly_total / 12
        print("Yearly Total: " + yearly_total)
        print("Monthly Average: " + monthly_average)
    print()


def edit_list(items): # defining edit list function
    month = input("Three-letter Month: ")
    if str(month) != len(3): # I'm getting an error message
        # "object of type 'int' has no len()" but the variable
        #"month" is clearly a string. Not sure what's going on here.
        print("Not a valid command. Please try again.\n")
    else:
        amount = input("Sales Amount: ")
        foo = []
        foo.append(month) # adding information to the csv file
        foo.append(amount)
        items.append(foo)
        write_items(items)
        print("Sales amount for " + month + " was modified.")
        print()
        
def display_menu(): # defining menu
    print("Monthly Sales Program")
    print()
    print("COMMAND MENU")
    print("monthly - View monthly sales")
    print("yearly  - View yearly sumary")
    print("edit - Edit sales for a month")
    print("exit - Exit program")
    print()

def main(): # defining main function
    display_menu()
    items = read_item()
    
    while True:        
        command = input("Command: ")
        if command.lower() == "monthly":
            monthly_list(items)
        elif command.lower() == "yearly":
            yearly_item(items)
        elif command.lower() == "edit":
            edit_list(items)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            
    print("Bye!")

if __name__ == "__main__":
    main()
