"""
Difficulty: 1
This program will ask the user for their name and their age.
The Program will then calculate in what year they will turn 100 years old.
The result will be printed in the console.
"""

name = input("State your name: ")
age = input("State your age: ")
y = 2018 - int(age) + 100
print("You will turn 100 in year: ", y)