# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("Enter your name: ")

# TODO: Ask the user for their age and store it in a variable
age = input("Enter your age: ")

# TODO: Print a greeting using the name and age variables
print(f"Hello, {name}! You are {age} years old.")

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("Enter the length of the rectangle: "))

# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("Enter the width of the rectangle: "))

# TODO: Calculate the area of the rectangle
area = length * width

# TODO: Print the result
print(f"The area of the rectangle is: {area}")

#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
# give an example of asking number from user in python
celsius = float(input("Enter temperature in Celsius: "))
print(f"Celsius entered: {celsius}")

# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

# TODO: Print the result rounded to two decimal places
print(f"{celsius}°C is equal to {round(fahrenheit, 2)}°F")

# some if else examples
num = 10
if num > 0:
    print("Positive number")   
else:
    print("Negative number or zero")

# ?another example: else if and elif
height = 175
if height < 150:    
    print("Short")  
elif height < 180:    
    print("Average height")
else:    
    print("Tall")

# ?another example: nested if with logical operators
age = 25
if age >= 18:
    if age < 65:
        print("Adult")
    else:
        print("Senior")
else:
    print("Minor")