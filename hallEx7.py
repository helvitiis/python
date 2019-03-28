# A. Hall
# Contact Manager Program

def list(contact_list): # def list fn
    if len(contact_list) == 0: # catch in case invalid input
        print("There are no contacts in the list.\n") # print confirmation
        return # restarts loop for valid input
    
    else:
        i = 1 # init 1
        for row in contact_list: # defining loop
            print(str(i) + ". " + row[0]) # prints number, period and spacer, then info
            i += 1 # adds +1 for loop
        print() # spacer

def add(contact_list): # def add fn
    name = input("Name: ") # input
    email = input("Email: ") # input
    phone = input("Phone: ") # input
    contact = [] # init empty list
    contact.append(name) # appending input
    contact.append(email) # appending input
    contact.append(phone) # appending input
    contact_list.append(contact) # appending new contact in list
    print(contact[0] + " was added.\n") # print confirmation

def view(contact_list): # def view fn
    number = int(input("Number: ")) # def number var with input
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.\n")
        
    else:
        contact = contact_list[number] # def contact var & grabbing position
        print("Name: " + contact[0], "\n", # print confirmation
              "Email: " + contact[1], "\n", # print confirmation
              "Phone: " + contact[2], "\n") # print confirmation

def delete(contact_list): # def delete fn
    number = int(input("Number: ")) # def number var with input
    if number < 1 or number > len(contact_list): # checks if input is invalid
        print("Invalid contact number.\n") # print confirmation
        
    else:
        contact = contact_list.pop(number-1) # removing contact with pop() fn
        print(contact[0] + " was deleted.\n") # print confirmation
      
def display_menu(): # display menu fn to list commands
    print("Contact Manager")
    print()
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()  

def main(): # init main fn
    contact_list = [["Guido van Rossum", "guido@guidovanrossum.com", "+12 34 5678 9999"],
                  ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"],
                    ["Rando Pers", "rando@erandopers.com", "+99 87 654 3210"],
                    ["Andy Meijers", "andy@andymeijers.com", "+88 33 284 0783"]]

    display_menu() # calling display fn
    
    while True: # loops for calling command fns       
        command = input("Command: ")
        if command == "list":
            list(contact_list)
        elif command == "add":
            add(contact_list)
        elif command == "del":
            delete(contact_list)
        elif command == "view":
            view(contact_list)
        elif command == "exit":
            break # breaks loop for exit
        else:
            print("Not a valid command. Please try again.\n") # print confirmation
            
    print("Bye!") # confirmation

if __name__ == "__main__": # call main fn
    main()
