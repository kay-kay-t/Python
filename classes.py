# Class is a blueprint fro creating new objects;
# object is an instance of a class
# To name classes we use pascal convention
# All the methods we define in a class should have at least one parameter,
# which we call "self" by convention. Self is a reference to a currant object

from collections import namedtuple


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))

# Constructor - special method that is called when we create a new point object
# Magic methods


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")


point = Point(1, 2)
print(point.x)

# Instance vs class attributes


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()

another = Point(3, 4)
another.draw()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Using decorater to extend behavior of a method or function

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()

# __str__ magic method
   def __str__(self):
        return f"({self.x}, {self.y})"

# __eq__ & __ gt__ magic methods

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(3, 4)
other = Point(1, 2)
print(point == other)
print(point > other)

# Arithmetic Operations

   def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(3, 4)
other = Point(1, 2)
combined = point + other
print(combined.x)

# Making custom containers (data structures)

class TagCloud:
    def __init__(self):  # Define a constructor
        self.tags = {}   # Initialize tags attributes to an empty dictionary

    def add(self, tag):  # Checking to see if we have this tag in our dictionary
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
# ^^^ we use a get method to get an item by this key and supply a default value if we dont have them
#  then we get a count incremented by 1
# and finally we set a value for this key
# and set fix case sensativity


# Get item method

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
# Set item method: three parametrs (self, key, value)

    def __setitem__(self, tag, count):
        # now we can set a number of given tag
        self.tags[tag.lower()] = count
 # To get the number of items in this tag cloud len method

    def __len__(self):
        return len(self.tags)
# To make it itterable so we can use for loops; we can iter - a build in function

    def _iter_(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

# Ther's a problem with this class. It dives us access to the underlying dictionary,
# that is used to keep track of the count of text. To fix this problem, we need to hide this attribute from the outside
# fn + F2 and change tags to __tags

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def _iter_(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.__tags["PYTHON"])
# This is how you make certain attributes privat

# Property function

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(-10)
print(product.price)

# Inheritance
#Parent, Base

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")
# To make other class inherit other, you just put other in brackets

#Child, Sub

class Mammal(Animal):
    def __init__(self):
    # Use super f, so this constructor f doesn't overrides parent constructor f
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()

# instance function & subclass function
print(isinstance(m, Mammal))
print(issubclass(Mammal, Animal))

# Extending built in types

class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())


class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

liast = TrackableList()
list.append("1")

# Named tuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
