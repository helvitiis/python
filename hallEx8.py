#!/usr/bin/python
# A. Hall
# Email List Cleaner
import csv

def display_title():
    print('Welcome to the Email List Cleaner')
    print()

def cleaner():
    print('Enter the source list name')
    filename = input('Source list: ') # prospects.csv
    print()
    print('Enter the cleaned list name')
    filename_out = input('Cleaned list: ') # prospects_clean
    print()
    print('Working.....\n')

    with open(filename, 'r') as inp, open(filename_out, 'w') as out:
        
        for row in inp:
            row.strip(' ') # strip whitespace
            row.title()
            
            if row.__contains__('@'):
                row.lower() # lowercase
                
            else: # title for names
                pass
                
        out.write(row)

def main():
    display_title()
    cleaner()

    print('Congratulations! Your list has been cleaned!')

if __name__ == '__main__':
    main()
