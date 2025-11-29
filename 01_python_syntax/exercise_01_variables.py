# Exercise 01: Variables and Basic Types
#
# Learning points:
# - How to create variables
# - Integer, float, and string types
# - Printing values
# - Printing different styles
#
# Steps:
# 1. Create three variables: age (int), height (float), name (str)
# 2. Print each variable on a separate line
# 3. Print a sentence combining them (string formatting)

age = 25
height = 1.80
name = "Selman"

print(age)
print(height)
print(name)

print(age, end = ' ')
print(height, end = '\t')
print(name, end = '\n')

print(f"My name is {name}, I am {age} years old and my height is {height} meters.")
