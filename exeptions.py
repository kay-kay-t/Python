try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age can't be 0")
# Or:
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")


else:
    print("No exceptions were thrown")

 # To use a function after exceptions (like close a file):
 try:
     file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")
finally:
    file.close()

# Or you can use with statement to relese resources (so no need in finally cloth)
with open("app.py") as file:
    print("File opened")


# from timeit import timeit
# with this function you can see execution time of code
