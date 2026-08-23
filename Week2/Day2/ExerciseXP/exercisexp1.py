# Exercise 1: Pets
# Key Python Topics:

# Inheritance
# Class instantiation
# Lists
# Polymorphism


# Instructions:

# Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
# See the example below, before diving in.



# Step 1: Create the Siamese Class

# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.


# Step 2: Create a List of Cat Instances

# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.


# Step 3: Create a Pets Instance

# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.


# Step 4: Take Cats for a Walk

# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.
# Step 1: Create the Siamese class

# Step 2: Create a list of cat instances

# Step 3: Create a Pets instance of the list of cat instances

# sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
# sara_pets.walk()

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Siamese(Cat):
    pass

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_obj = Bengal ('Benny', 2)
chartreux_obj = Chartreux ('Cherry', 4)
siamese_obj = Siamese ('Sassy', 6)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets (all_cats)

sara_pets.walk ()

# Exercise 2: Dogs
# Goal: Create a Dog class with methods for barking, running speed, and fighting.



# Key Python Topics:

# Classes and objects
# Methods
# Attributes


# Instructions:

# Step 1: Create the Dog Class

# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “<dog_name> is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.


# Step 2: Create Dog Instances

# Create three instances of the Dog class with different names, ages, and weights.


# Step 3: Test Dog Methods

# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark (self):
        return f'{self.name} is barking'

    def run_speed (self):
        dog_speed = self.weight / self.age * 10 
        return dog_speed
        
    def fight (self, other_dog):
        strength1 = self.run_speed () * self.weight
        strength2 = other_dog.run_speed () * other_dog.weight
        if strength1 > strength2:
            return f'{self.name} won'
        else:
            return f'{other_dog.name} won'

dog1 = Dog ('Dog1', 1, 7)
dog2 = Dog ('Dog2', 2, 8)
dog3 = Dog ('Dog3', 3, 9)

print (dog1.bark ())
print (dog2.bark ())
print (dog3.bark ())

print (dog1.run_speed())
print (dog2.run_speed())
print (dog3.run_speed())

print (dog1.fight(dog2))
print (dog1.fight(dog3))
print (dog2.fight(dog3))
