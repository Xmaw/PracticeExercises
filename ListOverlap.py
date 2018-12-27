"""
Take two lists and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates).
Make sure your program works on two lists of different sizes.
"""
import random

a = []
b = []

a_size = random.randrange(50)
for num in range(1, a_size):
    a.append(random.randrange(100))

b_size = random.randrange(50)
for num in range(1, b_size):
    b.append(random.randrange(100))

l_overlap = []
for number in a:
    if b.__contains__(number) and not l_overlap.__contains__(number):
        l_overlap.append(number)

print(l_overlap)
