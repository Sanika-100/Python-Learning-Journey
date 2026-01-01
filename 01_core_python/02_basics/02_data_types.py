# TEXT TYPE
name = "Sanika"
print(name, type(name))


# NUMERIC TYPES
# int
age = 21
print(age, type(age))

# float
price = 99.99
print(price, type(price))

# complex
number = 3 + 4j
print(number, type(number))


# SEQUENCE TYPES
# list
languages = ["Python", "Java", "C++"]
languages.append("JavaScript")
print(languages, type(languages))

# tuple
coordinates = (10, 20, 30)
print(coordinates, type(coordinates))

# range
numbers = range(1, 6)
print(list(numbers), type(numbers))


# MAPPING TYPE
student = {
    "name": "Sanika",
    "branch": "IT",
    "year": 2025
}
print(student, type(student))


# SET TYPES
# set
colors = {"red", "blue", "green", "red"}
print(colors, type(colors))

# frozenset
fixed_numbers = frozenset([1, 2, 3, 4])
print(fixed_numbers, type(fixed_numbers))


# BOOLEAN TYPE
is_active = True
print(is_active, type(is_active))


# BINARY TYPES
# bytes
data_bytes = b"Hello"
print(data_bytes, type(data_bytes))

# bytearray
data_bytearray = bytearray(5)
print(data_bytearray, type(data_bytearray))

# memoryview
data = bytes(5)
memory = memoryview(data)
print(memory, type(memory))


# NONE TYPE
result = None
print(result, type(result))


# -------------------- OUTPUT --------------------
# Sanika <class 'str'>
# 21 <class 'int'>
# 99.99 <class 'float'>
# (3+4j) <class 'complex'>
# ['Python', 'Java', 'C++', 'JavaScript'] <class 'list'>
# (10, 20, 30) <class 'tuple'>
# [1, 2, 3, 4, 5] <class 'range'>
# {'name': 'Sanika', 'branch': 'IT', 'year': 2025} <class 'dict'>
# {'green', 'red', 'blue'} <class 'set'>
# frozenset({1, 2, 3, 4}) <class 'frozenset'>
# True <class 'bool'>
# b'Hello' <class 'bytes'>
# bytearray(b'\x00\x00\x00\x00\x00') <class 'bytearray'>
# <memory at 0x...> <class 'memoryview'>
# None <class 'NoneType'>
