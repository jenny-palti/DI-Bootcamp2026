# Exercises XP - Week 2, Day 3 (OOP and Modules)
# Exercise 2 (Import) is in func.py and exercise_one.py
# Exercise 7 (Faker) is in faker_users.py

import random
import string
from datetime import date, datetime


# Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        raise TypeError("You can only add a number or a Currency")

    def __iadd__(self, other):
        self.amount = self + other
        return self


print("--- Exercise 1: Currencies ---")
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)          # 5 dollars
print(int(c1))     # 5
print(repr(c1))    # 5 dollars
print(c1 + 5)      # 10
print(c1 + c2)     # 15
print(c1)          # 5 dollars
c1 += 5
print(c1)          # 10 dollars
c1 += c2
print(c1)          # 20 dollars
try:
    print(c1 + c3)
except TypeError as error:
    print("TypeError:", error)


# Exercise 3: String module
print("\n--- Exercise 3: Random string ---")
letters = string.ascii_letters      # 'abc...zABC...Z'
random_string = ""
for _ in range(5):
    random_string += random.choice(letters)
print(random_string)


# Exercise 4: Current date
def show_current_date():
    print("Today is", date.today())


print("\n--- Exercise 4: Current date ---")
show_current_date()


# Exercise 5: Time left until January 1st
def time_until_new_year():
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    time_left = new_year - now
    print(f"Time left until January 1st: {time_left}")


print("\n--- Exercise 5: Until January 1st ---")
time_until_new_year()


# Exercise 6: Birthday and minutes
def minutes_lived(birthdate):
    # birthdate is a string in the format "YYYY-MM-DD", e.g. "1990-05-17"
    born = datetime.strptime(birthdate, "%Y-%m-%d")
    lived = datetime.now() - born
    minutes = int(lived.total_seconds() / 60)
    print(f"You have lived about {minutes:,} minutes.")


print("\n--- Exercise 6: Minutes lived ---")
minutes_lived("1990-05-17")
