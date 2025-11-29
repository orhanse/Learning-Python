# Exercise 01: Variables, Basic Types, and I/O
#
# Learning points:
# - Creating variables
# - Understanding int, float, and str types
# - Reading input from the user
# - Converting input to the correct type
# - Printing values
# - Using string formatting
#
# Steps:
# 1. Ask the user for their name and store it in a variable (str)
# 2. Ask the user for their age and convert it to an integer
# 3. Ask the user for their height and convert it to a float
# 4. Print each value on a separate line
# 5. Print a formatted sentence combining all variables
# 6. Add a simple condition:
#    - If age >= 18, print 'You are an adult'
#    - Else, print 'You are a minor'

# Step 1: User input for name
name = input('Enter your name: ')

# Step 2: User input for age
age = int(input('Enter your age: '))

# Step 3: User input for height
height = float(input('Enter your height in meters (e.g., 1.75): '))

# Step 4: Print each variable
print('Name:', name)
print('Age:', age)
print('Height:', height)

# Step 5: Print formatted sentence
print(f'My name is {name}, I am {age} years old, and my height is {height} meters.')

# Step 6: Conditional check
if age >= 18:
    print('You are an adult.')
else:
    print('You are a minor.')
