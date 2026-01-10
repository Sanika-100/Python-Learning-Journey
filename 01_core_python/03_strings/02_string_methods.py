# PYTHON STRING METHODS
# This file demonstrates commonly used string methods with simple examples


# MEMBERSHIP OPERATORS: in / not in
text = "Python Programming"
print("Python" in text)
print("Java" not in text)


# REMOVE WHITESPACE
data = "   hello world   "
print(data.strip())
print(data.lstrip())
print(data.rstrip())


# REPLACE
msg = "I like Java"
print(msg.replace("Java", "Python"))


# SPLIT
sentence = "Python is easy to learn"
print(sentence.split())


# PLACEHOLDER & MODIFIER (format)
name = "Sanika"
score = 95
print("Name: {}, Score: {}".format(name, score))
print("Name: {n}, Score: {s}".format(n=name, s=score))


# BASIC STRING METHODS
word = "python"

print(word.capitalize())
print(word.upper())
print(word.lower())
print(word.swapcase())
print(word.title())


# CHECKING METHODS
print(word.islower())
print(word.isupper())
print(word.isalpha())
print(word.isalnum())
print(word.isidentifier())


# COUNT & FIND
text2 = "python programming"
print(text2.count("p"))
print(text2.find("program"))
print(text2.rfind("p"))


# STARTSWITH / ENDSWITH
print(text2.startswith("python"))
print(text2.endswith("ing"))


# JOIN
languages = ["Python", "Java", "C++"]
print(", ".join(languages))


# CENTER / JUSTIFY
print(word.center(10, "-"))
print(word.ljust(10, "*"))
print(word.rjust(10, "*"))


# SPLITLINES
multi_line = "Hello\nPython\nWorld"
print(multi_line.splitlines())


# ZFILL
num = "42"
print(num.zfill(5))


# -------------------- OUTPUT --------------------
# True
# True
# hello world
# hello world
# hello world
# I like Python
# ['Python', 'is', 'easy', 'to', 'learn']
# Name: Sanika, Score: 95
# Name: Sanika, Score: 95
# Python
# PYTHON
# python
# PYTHON
# Python
# True
# False
# True
# True
# True
# 2
# 7
# 7
# True
# True
# Python, Java, C++
# --python--
# python****
# ****python
# ['Hello', 'Python', 'World']
# 00042
