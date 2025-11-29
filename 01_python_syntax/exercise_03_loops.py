# Exercise 03: Loops and Iteration Patterns
#
# Learning points:
# - Using for and while loops
# - Iterating through ranges, strings, and lists
# - Combining loops with conditionals
# - User input inside loops
# - Accumulating values
#
# Steps:
# 1. Ask the user to enter 5 numbers and store them in a list
# 2. Use a for loop to print each number
# 3. Use a for loop to print only numbers greater than 10
# 4. Calculate the sum of all numbers using a loop
# 5. Ask the user for a word and print each character on a separate line
# 6. Use a while loop to ask the user to enter numbers until they enter 0, then print the total sum

# Step 1: User inputs 5 numbers
numbers = []
for i in range(5):
    num = int(input(f'Enter number {i+1}: '))
    numbers.append(num)

# Step 2: Print each number
print('All numbers entered:')
for num in numbers:
    print(num, end = ' ')

# Step 3: Print numbers greater than 10
print('\n Numbers greater than 10:')
for num in numbers:
    if num > 10:
        print(num, end = '\t')

# Step 4: Calculate sum
total = 0
for num in numbers:
    total += num
print('\nSum of all numbers:', total)

# Step 5: Print characters of a word
word = input('Enter a word: ')
print('Characters in the word:')
for char in word:
    print(char, end = '-')
print('\n')

# Step 6: While loop for numbers until 0
sum_until_zero = 0
while True:
    n = int(input('Enter a number (0 to stop): '))
    if n == 0:
        break
    sum_until_zero += n
print('\nTotal sum of numbers entered:', sum_until_zero)
