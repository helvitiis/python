#!/usr/bin/env python3

tax = 0.06 # 'TAX' -> 'tax'

def sales_tax(total): # added colon [syntax error]
    sales_tax = total * tax
    return sales_tax # 'total' -> 'sales_tax'

def main():
    print("Sales Tax Calculator\n")
    total = float(input("Enter total: "))
    total_after_tax = round(total + sales_tax(total), 2)
    print("Total after tax: ", total_after_tax)
    
if __name__ == "__main__":
    main()
