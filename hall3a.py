# Program to find the sum of digits in a number

i = int(input("Please enter a value:")) # storing input in var i
sum = 0 # init var sum as 0

while(i > 0): # loop terminates if value of var i = 0
    foo = i % 10 # taking value of var i, finding the remainder with 10, and assigning value to var foo
    sum = sum + foo # adding sum of digits and var foo
    i = i //10 # dividing value of var i by 10

print("Sum of the number = %d" %sum) # outputting the sum
