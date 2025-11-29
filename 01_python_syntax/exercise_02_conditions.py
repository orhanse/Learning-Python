# Exercise 02: Conditions
#
# Learning points:
# - Using if/elif/else
# - Boolean expressions
#
# Steps:
# 1. Ask the user to enter a number (use input())
# 2. Convert it to an integer
# 3. If the number > 0 print "Positive"
# 4. If the number < 0 print "Negative"
# 5. If the number == 0 print "Zero"

intputVar = input('Enter a number: ')

# input() always gives a sting. You need to convert it to the type you need.
# In our case we convert it to int using int() function
number = int(intputVar)

if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')