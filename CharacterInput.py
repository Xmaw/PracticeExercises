"""
Difficulty: 1
This program will ask the user for their name and their age.
The Program will then calculate in what year they will turn 100 years old.
The result will be printed in the console.
"""

from datetime import datetime

name = input("State your name: ")
age = input("State your age: ")
times = input("How many times do you want it to be printed?")
current_year = datetime.now().year
y = current_year - int(age) + 100

for i in range(0, int(times)):
    print(name + ", you will turn 100 in year:", y)
