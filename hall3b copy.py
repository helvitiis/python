# Program to check if a number is a palindrome

num = int(input("Please enter a number: "))
 
tempVar = num # storing the input value, so that the original input is not disturbed
i = 0 # init var i
 
while tempVar > 0: # the while loop terminates if the input is 0
	i = (i * 10) + (tempVar % 10) # var i added to tempVar, modulo breaks tempVar
	tempVar = tempVar // 10 # dividing tempVar by 10
 
if num == i: # if the input value equals the value of variable i
	print("The number", num,"is a palindrome.")
else:
	print("The number", num,"is not a palindrome.")
