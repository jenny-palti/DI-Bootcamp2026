# Print the following output using one line of code:
print ('Hello world\nHello world\nHello world\nHello world\nHello world')

# Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8).
print((99**3) * 8) 

# 5 < 3  False
# 3 == 3 True
# 3 == "3" False
# "3" > 3 False
# "Hello" == "hello" False

# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."
computer_brand = 'Mac'
print (f'I have a {computer_brand} computer')

# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.
name = 'Jenny'
age = 42
shoe_size = 38
info = f'My name is {name}, I am {age} years old, and my shoe size is {shoe_size}'
print (info)

# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World".
a = 7
b = 5
if a > b:
   print("Hello World")

# Write code that asks the user for a number and determines whether this number is odd or even.
number = int(input("Tell me a number: "))
if number % 2 == 0:
   print(f"{number} is an even number")
else:
  print(f"{number} is an odd number")

# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.
name = input('What is your name?')
if name == 'Jenny':
    print ('What a coincidence')

# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.
height = int(input('What is your height in cm?'))
if height > 145:
       print ("You are tall enough to ride")
else:
       print ("You need to grow some more")