# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
Fruits = ["apple", "orange", "banana", "kiwi"]

# TODO: Use a for loop to print each fruit in the list
print("Question 1: Fruits List")
for fruit in Fruits:
    print(fruit)

    # Question 2: Using a while loop for countdown

print("\nQuestion 2: Countdown from 10")

count = 10
while count >= 0:
        print(count)
        count -= 1

# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
print("\nQuestion 3: First 10 Square Numbers")
for i in range(1, 11):
    print(f"The square of {i} is: {i ** 2}")

# Question 4: Using the random module

# TODO: Import the random module
import random

# TODO: Create a list of colors
colours = ["blue", "black", "red", "yellow"]

# TODO: Use a for loop to select and print 3 random colors from the list
print("\nQuestion 4: 3 Random Colors")
for _ in range(3):
     print(random.choice(colours))

# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero is not allowed."
#     return a / b

# TODO: Import the custom module and use its functions
import math_operations

print("\nQuestion 5: Custom Module Functions")
print(f"10 + 5 = {math_operations.add(10, 5)}")
print(f"10 - 5 = {math_operations.subtract(10, 5)}")
print(f"10 * 5 = {math_operations.multiply(10, 5)}")
print(f"10 / 5 = {math_operations.divide(10, 5)}")

# TODO: Use a while loop to create a simple calculator
print("\nSimple Calculator")
print("Type 'quit' to exit the calculator loop.")
while True:
    operation = input("Enter operation (+, -, *, /) or 'quit': ").strip().lower()
    
    if operation == 'quit':
        print("Goodbye! Thanks for using the calculator.")
        break
        
    if operation in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == '+':
                print(f"Result: {math_operations.add(num1, num2)}")
            elif operation == '-':
                print(f"Result: {math_operations.subtract(num1, num2)}")
            elif operation == '*':
                print(f"Result: {math_operations.multiply(num1, num2)}")
            elif operation == '/':
                print(f"Result: {math_operations.divide(num1, num2)}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    else:
        print("Invalid operation. Please try again.")