# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
Fruits = ["apple", "banana", "peach"]

# TODO: Add a fruit to the end of the list
Fruits.append("orange")

# TODO: Insert a fruit at the beginning of the list
Fruits.insert(0,"lemon")

# TODO: Remove a fruit from the list
Fruits.remove("peach")

# TODO: Print the modified list
print("Question 1: Final modified Fruits List")
print(Fruits)

# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1,2,3,4,5]

# TODO: Create a new list with each number squared
squared_numbers = [num ** 2 for num in numbers]

# TODO: Find the sum and average of the original numbers
total = sum(numbers)
average = total / len(numbers)

# TODO: Print the results
print("\nQuestion 2: List Operations")
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")
print(f"Sum: {total}, Average: {average}")

# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
capitals = {
    "South Africa": "Cape Town",
    "France": "Paris",
    "Japan": "Tokyo"
}

# TODO: Add a new country-capital pair
capitals["Germany"] = "Berlin"

# TODO: Update the capital of an existing country
capitals["South Africa"] = "Pretoria"

# TODO: Remove a country-capital pair
del capitals["France"]

print("\nQuestion 3: Final modified Capitals Dictionary")
print(capitals)

# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

# TODO: Print all the fruits (keys)
print("\nQuestion 4: Dictionary Operations")
print("Fruits:")
for fruit in fruit_colors:
    print(f" - {fruit}")

# TODO: Print all the colors (values)
print("Colors:")
for color in fruit_colors.values():
    print(f" - {color}")

# TODO: Print each fruit and its color
print("Fruit Colors:")
for fruit, color in fruit_colors.items():
    print(f" - {fruit}: {color}")

# TODO: Check if a fruit is in the dictionary and print its color
print("Checking for a specific fruit:")
search_fruit = "banana"
if search_fruit in fruit_colors:
    print(f"The color of {search_fruit} is {fruit_colors[search_fruit]}.")
else:
    print(f"{search_fruit} is not in the dictionary.")