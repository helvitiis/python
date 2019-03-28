# Ally Hall
import hall5a as st
import itertools # importing a library for infinite range loop
x = itertools.count() # assigning the count() function to x for inf range

def main(): # defining main function
    st.print_welcome() # init welcome function
    again = "y"
    while again.lower() == "y": # forces lowercase input & begins while loop
        item_cost = 0.0
        
        while item_cost != 0: # inits loop while the input is not 0
            item_total = 0.0
            
            def get_items_total():
                for i in range(x): # runs the for loop to collect input for an infinite amount of times until the input value is 0
                    item_cost = float(input("Cost of item: ")) # input for the item cost
                    item_total += i # adding stored item values
                    
                return get_items_total() # gets items for storing
        
        else: # completes loop to output final values
            print("Total: ", st.total_after_tax)
            print("Sales tax: ", st.tax_rate)
            print("Total after tax: ", st.total_after_tax)
        
        again = input("Again? (y/n): ")
        print()
        
        if again.lower() == "n": # breaks loop
            print("Thanks, bye!")

if __name__ == "__main__": # defining main statement
    main()
