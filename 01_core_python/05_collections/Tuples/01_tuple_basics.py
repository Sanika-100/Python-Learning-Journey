# PYTHON TUPLES
# Tuples are used to store multiple items in a single variable
# Tuples are ordered, immutable, and allow duplicate values


# CREATE A TUPLE
subjects = ("Math", "Physics", "Chemistry")
print(subjects)
# Output: ('Math', 'Physics', 'Chemistry')


# ACCESS TUPLE ITEMS
print(subjects[0])
# Output: Math

print(subjects[-1])
# Output: Chemistry


# ALLOW DUPLICATES
numbers = (1, 2, 2, 3)
print(numbers)
# Output: (1, 2, 2, 3)


# TUPLE LENGTH
print(len(subjects))
# Output: 3


# TUPLE WITH DIFFERENT DATA TYPES
mixed = ("Python", 3.10, True)
print(mixed)
# Output: ('Python', 3.10, True)


# TYPE OF TUPLE
print(type(subjects))
# Output: <class 'tuple'>


# SINGLE ITEM TUPLE (IMPORTANT)
single = ("AI",)
print(single)
# Output: ('AI',)


# LOOP THROUGH TUPLE
for item in subjects:
    print(item)
# Output:
# Math
# Physics
# Chemistry