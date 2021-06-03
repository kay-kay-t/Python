from pprint import pprint
import string
count = 0
for number in range(1, 20):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")


# ---- Fizz_buzz algorithm----
def fizz_buzz(input):
    if(input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif (input % 3 == 0):
        return "Fizz"
    elif (input % 5 == 0):
        return "Buzz"
    return input


print(fizz_buzz(15))


# ---Common interview question---Print the most frequently used letter
# My tries
string.ascii_lowercase

sentence = set("This is a common interview question")
alphabet = set(map(chr, range(97, 123)))
letter = sentence[]
totalLetters = (sentence & alphabet)
print(totalLetters)
count = 0
letter2 = totalLetters[]
if (letter == letter2):
    count = count+1
print(count)

# # Correct way:
sentence = "This is a common interview question"
# Using dictionary to find out frequency
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1)
# Now we are getting a list of tuples, to sort it, since we cannot sort dictionaries
# Using lambda f, where kv(key value) is a parametr & kv[1] is a value; sorting in decending order
char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda kv: kv[1], reverse=True)
# Printing the most repeating letter
print(char_frequency_sorted[0])
