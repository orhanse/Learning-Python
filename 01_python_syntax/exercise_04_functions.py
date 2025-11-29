# Exercise 04: Functions
#
# Learning points:
# - How to define a function using def
# - Function parameters and return values
# - Using functions with loops and conditionals
#
# Steps:
# 1. Define a function to calculate the square of a number
# 2. Define a function to check if a number is positive, negative, or zero (returns a string)
# 3. Define a function to calculate the sum of a list of numbers
# 4. Ask the user to input 5 numbers and store them in a list
# 5. Use a loop to print each number and its square (using the square function)
# 6. Use a loop to print if each number is positive, negative, or zero (using the check function)
# 7. Calculate the total sum of the list using the sum function and print it

# Step 1: Function to calculate square
def square(num):
    return num * num

# Step 2: Function to check number sign
def check_number(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'

# Step 3: Function to sum a list
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

# Step 4: User inputs 5 numbers
numbers = []
for i in range(5):
    n = int(input(f'Enter number {i+1}: '))
    numbers.append(n)

# Step 5: Print number and its square
print('\nNumber and its square:')
for num in numbers:
    print(f'{num} squared is {square(num)}')

# Step 6: Print number sign
print('\nNumber signs:')
for num in numbers:
    print(f'{num} is {check_number(num)}')

# Step 7: Print total sum
print('\nTotal sum of numbers:', sum_list(numbers))
