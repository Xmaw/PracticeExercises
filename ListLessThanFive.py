"""
This program will take a list of integers as an input and prints all elements that are lower than 5.

Extra 1: Instead of printing the elements one by one, make a new list that has all the elements less
         than 5 from this list in it and print out this new list.

Extra 2: Write this in one line of Python.

Extra 3: Ask the user for a number and return a list that contains only elements from the original list
         a that are smaller than that number given by the user.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Extra 2:
print([number for number in a if number < 5])

# Extra 1 & 3.
print("You will be asked to state a number. The program will then list each element in a predefined list\n"
      "That is less than the limit you have stated.")
limit = int(input("State the limit: "))
for number in a:
    if number < limit:
        print(number)
