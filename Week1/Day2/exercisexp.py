# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers
my_fav_numbers = {2, 4, 6, 8}
my_fav_numbers.add(10)
my_fav_numbers.add(12)
my_fav_numbers.remove(12)
friend_fav_numbers = {20, 30, 40}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Given a tuple of integers, try to add more integers to the tuple.
numbers1 = (1, 2, 3)
numbers2 = (4, 5)
numbers_final = numbers1 + numbers2
print(numbers_final)

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?
numbers = []

for number in range(3, 11):
    numbers.append(number / 2)

print(numbers)

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.
numbers = range(1, 21)

for number in numbers:
    print(number)

for number in range(2, 21, 2):
    print(number)

# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
while True:
    name = input("Please enter your name")

    if name.isdigit() or len(name) < 3:
        print("Please enter a name with at least 3 letters.")
    else:
        print("Thank you")
        break

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"
fruit_list = input("What are your favorite fruits? ").split()

any_fruit = input("Tell me any fruit: ")

if any_fruit in fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping, or type 'quit' to finish: ")

    if topping == "quit":
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + (len(toppings) * topping_price)

print("Your toppings are:", toppings)
print(f"Total cost: {total_cost}")

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_ticket_cost = 0

while True:
    age = input("Enter a person's age or type 'quit': ")

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    total_ticket_cost = total_ticket_cost + ticket_price

    print(total_ticket_cost)
    

