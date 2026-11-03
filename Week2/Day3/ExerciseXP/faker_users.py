# Exercise 7: Faker module
# Before running this file, install faker once:  pip3 install faker

from faker import Faker

fake = Faker()
users = []


def add_users(number_of_users):
    for _ in range(number_of_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code(),
        }
        users.append(user)


add_users(3)
print(users)
