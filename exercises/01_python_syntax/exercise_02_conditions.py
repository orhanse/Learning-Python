# Exercise 02: Conditionals and Logical Operators
#
# Learning points:
# - Using if/elif/else
# - Comparison operators: ==, !=, >, <, >=, <=
# - Logical operators: and, or, not
# - Combining conditions
# - Using user input
#
# Steps:
# 1. Ask the user to enter a number
# 2. Convert the input to an integer
# 3. Check if the number is positive, negative, or zero using if/elif/else
# 4. Ask the user for another number
# 5. Check if both numbers are positive using 'and'
# 6. Check if at least one number is zero using 'or'
# 7. Demonstrate 'not' operator by checking if the first number is NOT negative

# Step 1 & 2: User input
num1 = int(input('Enter the first number: '))

# Step 3: Positive, negative, or zero
if num1 > 0:
    print('The number is positive.')
elif num1 < 0:
    print('The number is negative.')
else:
    print('The number is zero.')

# Step 4: Second number input
num2 = int(input('Enter the second number: '))

# Step 5: Check if both numbers are positive
if num1 > 0 and num2 > 0:
    print('Both numbers are positive.')

# Step 6: Check if at least one number is zero
if num1 == 0 or num2 == 0:
    print('At least one number is zero.')

# Step 7: Using 'not' operator
if not num1 < 0:
    print('The first number is not negative.')
