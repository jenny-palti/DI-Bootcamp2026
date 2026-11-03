# Daily Challenge: Circle - Week 2, Day 3

import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Give a radius or a diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


c1 = Circle(radius=3)
c2 = Circle(diameter=10)
c3 = Circle(radius=1)

print(c1)                          # Circle(radius=3, diameter=6)
print(c2)                          # Circle(radius=5.0, diameter=10.0)
print("Radius of c2:", c2.radius)
print("Diameter of c1:", c1.diameter)
print("Area of c1:", round(c1.area(), 2))

print("c1 + c2 =", c1 + c2)
print("Is c2 bigger than c1?", c2 > c1)
print("Is c1 equal to Circle(diameter=6)?", c1 == Circle(diameter=6))

circles = [c1, c2, c3]
circles.sort()
print("Sorted:", circles)
