"""
Take two lists and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates).
Make sure your program works on two lists of different sizes.
"""
import random

a = random.sample(range(1, 100), random.randrange(50))
b = random.sample(range(1, 100), random.randrange(50))
l_overlap = [over for over in a if b.__contains__(over)]

print(l_overlap)
