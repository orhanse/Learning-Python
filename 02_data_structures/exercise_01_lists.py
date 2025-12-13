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
# 1. Create a list with initial values [3, 7, 12, 5, 9, 12]
# 2. Access elements using index
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
print('Step-1: Creating a list')

numbers = [3, 7, 12, 5, 9, 12] #lists allows dublicate values
print('Initial list:', numbers)
print('-----------')

# Step 2: Access elements using index
print('Step-2: Access elements')

print('First element:', numbers[0])  # Access first element
print('Last element:', numbers[-1])  # Access last element
print('2nd, 3rd and 4nd elements:', numbers[1:4]) #Elements from index 1 to index 4 (index 4 is not included)
print('1st and 2th elements:', numbers[:2]) #Elements from index 0 to index 2 (index 2 is not included)
print('Elements from last 4 to last 2:', numbers[-4:-1]) # Element from index -4 to index -2 (index -1 is not included)

#using 'in' you can check if an item is exist
number = int(input('Enter a number to find in the list: '))
if number in numbers:
    print(f'{number} is in the numbers list.' )
else:
    print(f'{number} is NOT in the numbers list.')
print('-----------')

# Step 3: Update an element
print('Step-3: Update an element')

numbers[3] = 15  # Change the 3rd element
print('Updated list (4th element changed to 15):', numbers)

numbers[1:3] = [42, 12] # Replacing values in index 1 and index 2 with the new values. 
print('Updating list (2nd and 3rd elements changes to 42 and 12):', numbers)
print('-----------')

# Step 4: Delete an element
print('Step-4: Deleting elements')

del numbers[1]  # Delete the 2nd element
print('After DELETING 2nd element:', numbers)

numbers.remove(12) # Remove the first element with the given value (12)
print('After REMOVING the first element with the value of 12:', numbers)

numbers.pop(2) #Pop the element at the index 2
print('After POPING the 3rd element:', numbers)

numbers.pop() # Pop the last element in the list
print('After POPING the last element:', numbers)

numbers.clear() # Clear the list
print('After CLEARING the list: ', numbers)
print('-----------')

# Step 5: Slice the list
print('Step-5: Slice the list')
numbers = [2, 4, 6, 8, 42]
print('First 3 elements:', numbers[:3])  # Slice first 3
print('Last 2 elements:', numbers[-2:])  # Slice last 2
print('-----------')

# Step 6: Append and insert elements
print('Step-6: Append and insert elements')
numbers.append(20)  # Add to the end
numbers.insert(1, 8)  # Insert at index 1
print('After append(20) and insert(8):', numbers)
print('-----------')

# Step 7: Iterate through the list and print elements > 10
print('Step-7: Iterate through the list and print elements > 10')
print('Numbers greater than 10:')
for num in numbers:
    if num > 10:
        print(num)
print('-----------')

# Step 8: Use built-in functions
print('Step-8: Use build-in functions')
print('Length of list:', len(numbers))
print('Sum of numbers:', sum(numbers))
print('Maximum value:', max(numbers))
print('Minimum value:', min(numbers))
print('-----------')

# Step 9: Nested list example
print('Step-9: Nested list example')
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Nested list:', nested_list)
print('Access element 5:', nested_list[1][1])  # Access inner element
print('-----------')

# Step 10: Combine lists
print('Step-10: Combine lists')
more_numbers = [100, 200, 300]
combined = numbers + more_numbers
print('Combined list:', combined)
print('-----------')

# Step 11: Define a function to get even numbers from a list
print('Step-11: Defining a function to get even numbers from a list')
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
print('-----------')

# Step 12: User input to add numbers
print('Step-12: User input to add numbers')
user_input = input('Enter a number to add to the list: ')  # Read input
numbers.append(int(user_input))  # Add to list
print('Updated list with user input:', numbers)
print('-----------')
