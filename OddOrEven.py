"""
This program will take a number as input from the user and it will print if the number is odd or even.
If the number is a multiple of 4, the output will be altered from the 'even' output.
"""

number = int(input("State an odd or an even number: "))
if number % 4 == 0:
    print(number, "is a multiple of 4 and it is even.")
elif number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")
