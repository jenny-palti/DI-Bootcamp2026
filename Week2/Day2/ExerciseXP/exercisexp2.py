# Step 1: Import the Dog Class

# In a new Python file, import the Dog class from the previous exercise.


# Step 2: Create the PetDog Class

# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “<dog_names> all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.


# Step 3: Test PetDog Methods

# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.

import random
from exercisexp1 import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = [self.name]

        for dog in args:
            dog_names.append(dog.name)

        names = ", ".join(dog_names)
        print(f"{names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]

            random_index = random.randint(0, len(tricks) - 1)
            random_trick = tricks[random_index]

            print(f"{self.name} {random_trick}")


fido = PetDog("Fido", 2, 10)
buddy = PetDog("Buddy", 4, 20)
max_dog = PetDog("Max", 3, 15)

fido.train()
fido.play(buddy, max_dog)
fido.do_a_trick()

# Step 1: Create the Person Class

# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.


# Step 2: Create the Family Class

# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)


# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.


# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."


# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.


# Expected Behavior:

# Once implemented, your program should allow you to:

# Create a family with a last name.
# Add members to the family using the born() method.
# Use check_majority() to see if someone is allowed to go out.
# Display family information with family_presentation().
# Don’t forget to test your classes by creating an instance of Family, adding members, and calling each method to see the expected output

# Exercise 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"There is no {first_name} in the {self.last_name} family.")

    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for person in self.members:
            print(f"- {person.first_name}, {person.age} years old")


smith_family = Family("Smith")
smith_family.born("Emma", 20)
smith_family.born("Leo", 12)

smith_family.check_majority("Emma")
smith_family.check_majority("Leo")
smith_family.family_presentation()
