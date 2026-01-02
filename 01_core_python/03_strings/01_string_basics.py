# PYTHON STRINGS
# Strings are sequences of characters enclosed in single or double quotes

# Creating strings
text1 = "Hello"
text2 = 'Python'
print(text1)
print(text2)


# STRING LENGTH
# len() returns the number of characters in a string
message = "Python Programming"
print(len(message))


# STRING INDEXING
# Indexing starts from 0
word = "Python"
print(word[0])
print(word[1])
print(word[-1])   # negative index starts from end


# STRING SLICING
# Used to extract part of a string
print(word[0:4])
print(word[2:6])
print(word[:3])
print(word[3:])
print(word[-4:-1])


# MODIFY STRINGS
# Strings are immutable, methods return new strings
sample = " hello world "
print(sample.upper())
print(sample.lower())
print(sample.strip())
print(sample.replace("world", "Python"))


# CONCATENATE STRINGS
# Joining strings using +
a = "Hello"
b = "World"
print(a + " " + b)


# FORMAT STRINGS
# Used to insert variables into strings
name = "Sanika"
age = 22

print("My name is {} and I am {}".format(name, age))
print(f"My name is {name} and I am {age}")   # f-string (recommended)


# ESCAPE CHARACTERS
# Used to insert special characters in strings
print("Python is \"easy\" to learn")
print("It\'s a powerful language")
print("This is a new line\nPython")
print("Tabbed\tText")


# STRING METHODS
# Built-in functions to perform operations on strings
text = "python programming"

print(text.capitalize())
print(text.title())
print(text.count("p"))
print(text.find("program"))
print(text.startswith("python"))
print(text.endswith("ing"))
print(text.islower())
print(text.isupper())
print(text.split())


# STRING EXERCISES
# Practice-style examples
sentence = "Learning Python is fun"

print(sentence[::-1])              # reverse string
print("Python" in sentence)        # membership check
print(sentence.replace("fun", "awesome"))


# -------------------- OUTPUT --------------------
# Hello
# Python
# 18
# P
# y
# n
# Pyth
# thon
# Pyt
# hon
# pro
# HELLO WORLD
# hello world
# hello world
#  hello Python
# Hello World
# My name is Sanika and I am 22
# My name is Sanika and I am 22
# Python is "easy" to learn
# It's a powerful language
# This is a new line
# Python
# Tabbed	Text
# Python programming
# Python Programming
# 2
# 7
# True
# True
# True
# False
# ['python', 'programming']
# nuf si nohtyP gninraeL
# True
# Learning Python is awesome
