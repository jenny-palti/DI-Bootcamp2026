# Step 1: Define a Function
# Define a function named display_message().
# This function should not take any parameters.
# Step 2: Print a Message
# For example: “I am learning about functions in Python.”
# Step 3: Call the Function
# This will execute the code inside the function and print your message.
def display_message():
    print("I am learning about functions in Python.")

display_message()

# Step 1: Define a Function with a Parameter
# Define a function named favorite_book().
# This function should accept one parameter called title.
# Step 2: Print a Message with the Title
# The function needs to output a message like “One of my favorite books is <title>”.
# Step 3: Call the Function with an Argument
# Call the favorite_book() function and provide a book title as an argument.
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

title = "Harry Potter"

favorite_book(title)

# Step 1: Define a Function with Parameters ok
# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.
# Step 2: Print a Message
# Inside the function, set up the code to display a sentence like “ is in “.
# Replace <city> and <country> with the parameter values.
# Step 3: Call the Function
# Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")


describe_city("Tokyo", "Japan")
describe_city("Paris", "France")
describe_city("Jerusalem", "Israel")
describe_city("Atlantis")  # Uses the default country
# Exercise 4: Random
# Goal: Create a function that generates random numbers and compares them.

# Key Python Topics:

# random module
# random.randint() function
# Conditional statements (if, else)


# Step 1: Import the random Module

# At the beginning of your script, use import random to access the random number generation functions.


# Step 2: Define a Function with a Parameter

# Create a function that accepts a number between 1 and 100 as a parameter.


# Step 3: Generate a Random Number

# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.


# Step 4: Compare the Numbers

# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.


# Step 5: Call the Function

# Call the function with a number between 1 and 100.
import random


def compare_number(my_number):
    random_number = random.randint(1, 100)

    if my_number == random_number:
        print("Success! The numbers are the same.")
    else:
        print("Fail! The numbers are different.")
        print(f"Your number: {my_number}")
        print(f"Random number: {random_number}")


compare_number(50)

# Step 1: Define a Function with Parameters
# Define a function called make_shirt().
# This function should accept two parameters: size and text.

# Step 2: Print a Summary Message
# Set up the function to display a sentence summarizing the shirt’s size and message.

# Step 3: Call the Function

# Step 4: Modify the Function with Default Values
# Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.

# Step 5: Call the Function with Default and Custom Values
# Call make_shirt() to make a large shirt with the default message.
# Call make_shirt() to make a medium shirt with the default message.
# Call make_shirt() to make a shirt of any size with a different message.
# Step 1, 2, and 4: Define the function and print a summary

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")


# Step 5: Large shirt with the default message
make_shirt()

# Step 5: Medium shirt with the default message
make_shirt("medium")

# Step 5: Small shirt with a different message
make_shirt("small", "Coding is fun!")

# Step 1: Create a List of Magician Names
# Create a list called magician_names with the given names:
# ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Step 2: Create a Function to Display Magicians
# Create a function called show_magicians() that takes the magician_names list as a parameter.
# Inside the function, iterate through the list and print each magician’s name.

# Step 3: Create a Function to Modify the List
# Create a function called make_great() that takes the magician_names list as a parameter.
# Inside the function, use a for loop to iterate through the list and add “the Great” before each magician’s name.

# Step 4: Call the Functions
# Call make_great() to modify the list.
# Call show_magicians() to display the modified list.

magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]


def show_magicians(magician_names):
    for name in magician_names:
        print(name)


def make_great(magician_names):
    for index in range(len(magician_names)):
        magician_names[index] = magician_names[index] + " the Great"


make_great(magician_names)
show_magicians(magician_names)

# Step 1: Create the get_random_temp() Function
# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.

# Step 2: Create the main() Function
# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”

# Step 3: Provide Temperature-Based Advice
# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”

import random


def get_random_temp():
    random_temp = random.randint(-10, 40)
    return random_temp


def main():
    temperature = get_random_temp()

    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif temperature < 16:
        print("Quite chilly! Don't forget your coat.")
    elif temperature < 24:
        print("Nice weather.")
    elif temperature < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


main()