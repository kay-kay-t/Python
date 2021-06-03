# ------ Data Structures-------

# ----- Lists-----------
from sys import getsizeof
from array import array
from collections import deque
numbers = list(range(20))
print(numbers)
chars = list("Hello World")
print(chars)

# Will return every other number
numbers = list(range(20))
print(numbers[::2])

# Will return list in opposite order
numbers = list(range(20))
print(numbers[::-1])

# Unpacking/packing lists
numbers = [1, 2, 3]
first, second, third = numbers

numbers = [1, 2, 3, 4, 5, 6, 4, 3, 6]
first, second, *other = numbers
print(first)
print(other)
# *other can be in the middle as well followed by last

# Loop over lists
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)
letters = ["a", "b", "c"]
# To add to the end of the list
letters.append("d")
# To add to specific place
letters.insert(0)
# To remove from end
letters.pop(1)
# If you don't know the index
letters.remove("a")
# Delete statement, you can remove list of items
del letters[0:3]
# To remove all
letters.clear()
print(letters)


# Finding items
letters = ["a", "b", "c"]
if "d" in letters:
    print(letters.index("d"))

letters = ["a", "b", "c"]
print(letters.count("d"))


# Sorting lists
numbers = [1, 23, 4, 56, 4, 3, 6]
# numbers.sort(reverse=True)
print(sorted(numbers))
print(numbers)

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# Better way (Lambda function: parametr:expression)
items.sort(key=lambda item: item[1])
print(items)


# Map function
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# prices = []
# for item in items:
#     prices.append(item[1])

prices = list(map(lambda item: item[1], items))
print(prices)

# Filter function
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# List Comprehensions
prices = [item[1] for item in items]

filtered = [item for item in items if item[1] >= 10]

# Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2)))

# ----------Stacks---LIFO behaviour-----Website session
browsing_session = []
browsing_session.append(1)  # method to add item to stack
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()  # method to remove item to stack
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])  # to take to previous page

# ------Queue------FIFO------Removing first item
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")

# ----Tuple - read-only list, used to srore sequence of objects---
point = 1, 2
point = ()  # empty tuple
point = tuple([1, 2])

# ---Swapping vars---
x = 10
y = 11

z = x
x = y
y = z
# Easier:
x, y = y, x
print("x", x)
print("y", y)

# ----Arrays-----used for bigger numbers of items

numbers = array("i", [1, 2, 3])
numbers[0]
# Every object in this array should be of the same type

# # -----Sets-----collection with no duplicates
numbers = [1, 1, 2, 3, 3, 4, ]
uniques = set(numbers)
second = {1, 4}
second.add(5)
len(second)
print(uniques)


# includes all the items which are in a first set or second set
print(first | second)
print(first & second)  # includes all the items that exist in both sets
print(first - second)  # difference of two sets
# return items that are eithe in a first or second, but not both
print(first ^ second)
# Set object doesnt support indexing

# -----Dictionaries-----collection of key value pairs
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
# or use get method
print(point.get("a"))

del point["x"]
print(point)

for key in point:
    print(key, point[key])

# Dictionary comprehensions
values = {}
for x in range(5):
    values[x] = x * 2

values = {x: x * 2 for x in range(5)}
print(values)

# ----- Generators-------

values = (x * 2 for x in range(5))
print("gen", getsizeof(values))

# ----Unpacking operator '*'
numbers = [1, 2, 3]
print(*numbers)

values = [*range(5), *"Hello world"]
print(values)
