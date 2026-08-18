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