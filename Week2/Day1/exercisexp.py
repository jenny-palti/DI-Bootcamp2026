# # Instructions:

# # Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.
# Step 1: Create Cat Objects

# Use the Cat class to create three cat objects with different names and ages.

# Step 2: Create a Function to Find the Oldest Cat

# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

# Step 3: Print the Oldest Cat’s Details

# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age 
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 5)
cat3 = Cat("Shadow", 2)

# cat_list = [cat1, cat2, cat3] do we need a list here?

def find_oldest_cat(cat1, cat2, cat3):
    oldest_cat = cat1
    if cat2.age > oldest_cat.age:
        oldest_cat = cat2
    if cat3.age > oldest_cat.age:
        oldest_cat = cat3
    return oldest_cat 
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")   

# Step 1: Create the Dog Class
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")
davids_dog = Dog("Dudu", 50)
sarahs_dog = Dog("Sumsum", 30)

print (f'{davids_dog.name} is {davids_dog.height} cm tall.')
print (f'{sarahs_dog.name} is {sarahs_dog.height} cm tall.')

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

# dog_list = [davids_dog, sarahs_dog] do we need a list?
def biggest_dog (davids_dog, sarahs_dog):
    if davids_dog.height > sarahs_dog.height:
        return davids_dog
    else:
        return sarahs_dog
biggest_dog = biggest_dog(davids_dog, sarahs_dog)
print(f'The biggest dog is {biggest_dog.name}.')
# Instructions:
# Create a Song class with a method to print song lyrics line by line.
# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
lyrics = [
    "If there's something strange",
    "in your neighborhood",
    "who you gonna call",
    "Ghostbusters"
]
my_song = Song(lyrics)
my_song.sing_me_a_song()
# Step 1: Define the Zoo Class
# Create a class called Zoo.

# Implement the init() method:

# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.
# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.
# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.
# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.
# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals()
# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.
# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.
class Zoo:

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()

        self.animal_groups = {}

        for animal in self.animals:
            first_letter = animal[0]

            if first_letter not in self.animal_groups:
                self.animal_groups[first_letter] = []

            self.animal_groups[first_letter].append(animal)

    def get_groups(self):
        for letter, animals in self.animal_groups.items():
            print(letter, ":", animals)


# Create a Zoo object
my_zoo = Zoo("Central Zoo")

# Add animals
my_zoo.add_animal("cat")
my_zoo.add_animal("dog")
my_zoo.add_animal("lion")
my_zoo.add_animal("elephant")
my_zoo.add_animal("giraffe")

# Try adding a duplicate
my_zoo.add_animal("cat")

# Display animals
my_zoo.get_animals()

# Sell an animal
my_zoo.sell_animal("dog")

# Display animals again
my_zoo.get_animals()

# Sort and group animals
my_zoo.sort_animals()

# Display groups
my_zoo.get_groups()
