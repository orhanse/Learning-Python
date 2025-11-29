# Exercise 03: Loops
#
# Learning points:
# - Using for loops
# - Using while loops
# - Working with ranges
#
# Steps:
# 1. Use a for-loop to print numbers 1 to 5
# 2. Use a while-loop to print numbers 5 to 1
# 3. Print each character of a string in a loop

for i in range(1, 6):
    print(i)

count = 5
while count > 0:
    print(count)
    count -= 1

text = "Python"
for char in text:
    print(char)
