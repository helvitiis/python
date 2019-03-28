#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
score1 = int(input("Enter test score: "))
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))
# changing input from += assignment operator
# because the objects are not subscriptable

# calculate average score
average_score = round((score1 + score2 + score3) / 3)
total_score = score1 + score2 + score3
             
# format and display the result
print("======================")
print("Score #1:  ", score1)
print()
print("Score #2:  ", score2)
print()
print("Score #3:  ", score3)
print()
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)


