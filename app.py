# print("Helllo World")

# #-----Formated strings------
# first = "a"
# last = "b"
# full = f"{first} {last}"
# print(full)

# print(round(2.9))
# print(abs(-2.9))

# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# # int(x)
# # float(x)
# # bool(x)2
# # str(x)

# #-----Loops------

# for number in range(3):
#     print("Attempt", number + 1, (number + 1) * ".")
# # cleaner:
# for number in range(1, 4):
#     print("Attempt", number, number * ".")

# for x in "Python":
#     print(x)

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# #--------Functions--------
# #-----Creating your own function
# # 2 types of functions: perform a task function:
# def greet():
#     print("Hi there")


# greet()


# # #and return a value function:
# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("ABD")
# file = open("content.txt", "w")
# file.write(message)

# # Passing verieble number of arguments into a function
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))


# # Passing key word args (name = value) - a dictionary
# def save_user(**user):
#     # print(user)
#     print(user["id"])


# save_user(id=1, name="ABC", age=22)


# #----Debuging----
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#         return total


# print("Start")
# print(multiply(2, 3, 4, 5))

# # ----Shortcuts-----
# # To move cursor to the end of the line F10
# # To move cursor to the beginning of the line F9
# # To move to the beginning of the file ctrl + F9
# # To move to the end of the file ctrl + f10
# # To move the line up/ down alt + up/down
# # To duplicate: alt + shift + down
