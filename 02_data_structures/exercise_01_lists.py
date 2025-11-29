# Exercise 01: Lists and Basic Operations
#
# Learning points:
# - Creating, accessing, updating, and deleting list elements
# - List slicing and indexing
# - Iterating through lists with for loops
# - Using built-in list functions (len, sum, max, min)
# - Nested lists and multi-level access
# - Combining lists
# - Using functions to manipulate lists
#
# Steps:
# 1. Create a list with initial values [3, 7, 12, 5, 9]
# 2. Access elements using index: access first and last element
# 3. Update an element: change the 3rd element
# 4. Delete an element: remove the 2nd elemen
# 5. Slice the list: slice first 3 and slice the last 2 elements
# 6. Append and insert elements: add to the end and add to the index 1
# 7. Iterate through the list and print elements > 10
# 8. Use built-in functions: len, sum, max, min
# 9. Create a nested list example: and access to inner list element
# 10. Combine lists: create another list and combine it with the list create in step_1
# 11. Define a function to get even numbers from a list
#   11a. Initialize empty list
#   11b: Loop through list and check if element is even
#   11c: Return list of even numbers
# 12. User input to add numbers: read input, add to the list



# Step 1: Create a list with initial values
numbers = [3, 7, 12, 5, 9]
print('Initial list:', numbers)

# Step 2: Access elements using index
print('First element:', numbers[0])  # Access first element
print('Last element:', numbers[-1])  # Access last element

# Step 3: Update an element
numbers[2] = 15  # Change the 3rd element
print('Updated list (3rd element changed to 15):', numbers)

# Step 4: Delete an element
del numbers[1]  # Remove the 2nd element
print('After deleting 2nd element:', numbers)

# Step 5: Slice the list
print('First 3 elements:', numbers[:3])  # Slice first 3
print('Last 2 elements:', numbers[-2:])  # Slice last 2

# Step 6: Append and insert elements
numbers.append(20)  # Add to the end
numbers.insert(1, 8)  # Insert at index 1
print('After append(20) and insert(8):', numbers)

# Step 7: Iterate through the list and print elements > 10
print('Numbers greater than 10:')
for num in numbers:
    if num > 10:
        print(num)

# Step 8: Use built-in functions
print('Length of list:', len(numbers))
print('Sum of numbers:', sum(numbers))
print('Maximum value:', max(numbers))
print('Minimum value:', min(numbers))

# Step 9: Nested list example
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Nested list:', nested_list)
print('Access element 5:', nested_list[1][1])  # Access inner element

# Step 10: Combine lists
more_numbers = [100, 200, 300]
combined = numbers + more_numbers
print('Combined list:', combined)

# Step 11: Define a function to get even numbers from a list
def get_even_numbers(lst):
    # Step 11a: Initialize empty list
    evens = []
    # Step 11b: Loop through list and check if element is even
    for n in lst:
        if n % 2 == 0:
            evens.append(n)
    # Step 11c: Return list of even numbers
    return evens

print('Even numbers in combined list:', get_even_numbers(combined))

# Step 12: User input to add numbers
user_input = input('Enter a number to add to the list: ')  # Read input
numbers.append(int(user_input))  # Add to list
print('Updated list with user input:', numbers)
