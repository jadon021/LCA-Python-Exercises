# Question 1: Arithmetic and Assignment Operators

# Give variables values

x = 20
y = 5

# TODO: Add 3 to x using the += operator
x += 3

# TODO: Multiply y by 2 using the *= operator
y *= 2

# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y

# TODO: Print the value of 'result'
print(f"Question 1 Result: {result}\n")


# Question 2: Comparison and Logical Operators

# Give variables values

a = 20
b = 5
c = 10

# TODO: Create a condition that checks if a is greater than b
condition1 = a > b

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
condition2 = (b % 2 == 0)

# TODO: Create a condition that checks if c is less than or equal to a
condition3 = (c <= a)

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = condition1 or (condition2 and condition3)

# TODO: Print the value of 'final_condition'
print(f"Question 2 Final Condition: {final_condition}\n")

# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = float(input("Question 3 Enter a test score (0-100): "))

# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <=79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"

# TODO: Print the grade for the given score
print(f"Grade: {grade}\n")

# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation (+, -, *, /): ")

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+":
    operation_result = num1 + num2
    print(f"Result: {num1} + {num2} = {operation_result}")
elif operation == "-":
    operation_result = num1 - num2
    print(f"Result: {num1} - {num2} = {operation_result}")
elif operation == "*":
    operation_result = num1 * num2
    print(f"Result: {num1} * {num2} = {operation_result}")
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        operation_result = num1 / num2
        print(f"Result: {num1} / {num2} = {operation_result}")
else:
    print("Invalid operation entered. Please use +, -, *, or /.")