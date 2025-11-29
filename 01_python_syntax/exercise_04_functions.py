# Exercise 04: Functions
#
# Learning points:
# - Defining a function
# - Passing arguments
# - Returning values
#
# Steps:
# 1. Create a function add(a, b) that returns the sum
# 2. Create a function greet(name) that prints a greeting
# 3. Call both functions at the end of the file

def add(a, b):
    return a + b

def greet(name):
    print("Hello " + name)

# You can actually specify the type of a parameter
# and the type of the return type of a function like this
# It is important to understand defining parameter and return type does not raise a TypeError
# It can be used for documentation purposes,
# It helps IDEs do better autocompletion and find errors ahead of runtime by using static analysis
def multiply(x: float, y: int) -> float:
    return x * y

a = 10
b = 30.6

sum = add(a, b)
print (a, '+', b, '=', sum)

name = 'John'
greet(name)

answer = multiply(12, 23.5)
print('Answer: ', answer)