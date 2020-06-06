# Regular expressions

# Import regular expressions
import re

# mytext = "I am from Earth"

# USING REGULAR EXPRESSIONS TO FIND THE MATCH

# if re.search("Earth", mytext):
#     print("MATCH found")
# else:
#     print("MATCH not found")

# x = re.search("Earth", mytext)


# FIND THE START AND END INDEX OF THE MATCH

# print(x)
# print(type(x))

# print(x.start())
# print(x.end())

# USING REGULAR EXPRESSION TO SPLIT THE STRING.
# REMEMBER THAT THIS METHOD IS ALREADY BUILT INTO STRINGS.

# split_term = "@"
# email = "hello@gmail.com"

# output = re.split(split_term, email)
# print(output)

# FIND ALL INSTANCES OF THE MATCH.

# my_text = "the cat can walk like a cat, what else a cat can do?"

# x = re.findall("cat", my_text)
# print(x)

# You len() method to find the number of instances

# Meta 