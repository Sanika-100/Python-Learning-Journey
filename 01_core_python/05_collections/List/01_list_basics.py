# PYTHON LISTS
# Lists store multiple items in a single variable
# Lists are ordered, mutable, and allow duplicate values


# CREATE LIST
fruits = ["apple", "banana", "cherry"]
print(fruits)
# Output: ['apple', 'banana', 'cherry']


# ACCESS LIST ITEMS
print(fruits[0])
# Output: apple

print(fruits[-1])
# Output: cherry


# CHANGE LIST ITEMS
fruits[1] = "mango"
print(fruits)
# Output: ['apple', 'mango', 'cherry']


# ADD LIST ITEMS
fruits.append("orange")
print(fruits)
# Output: ['apple', 'mango', 'cherry', 'orange']

fruits.insert(1, "grapes")
print(fruits)
# Output: ['apple', 'grapes', 'mango', 'cherry', 'orange']


# REMOVE LIST ITEMS
fruits.remove("mango")
print(fruits)
# Output: ['apple', 'grapes', 'cherry', 'orange']

fruits.pop()
print(fruits)
# Output: ['apple', 'grapes', 'cherry']


# LOOP THROUGH LIST
for fruit in fruits:
    print(fruit)
# Output:
# apple
# grapes
# cherry

# ALLOW DUPLICATES
dup_list = ["apple", "banana", "apple", "cherry"]
print(dup_list)
# Output: ['apple', 'banana', 'apple', 'cherry']


# LIST LENGTH
print(len(dup_list))
# Output: 4


# LIST WITH DIFFERENT DATA TYPES
mixed_list = ["apple", 10, True, 5.5]
print(mixed_list)
# Output: ['apple', 10, True, 5.5]


# TYPE OF LIST
print(type(mixed_list))
# Output: <class 'list'>


# LIST CONSTRUCTOR
new_list = list(("red", "green", "blue"))
print(new_list)
# Output: ['red', 'green', 'blue']

# CHANGE RANGE OF ITEMS (SLICING)

colors = ["red", "blue", "green", "yellow", "black"]
colors[1:3] = ["white", "pink"]
print(colors)
# Output: ['red', 'white', 'pink', 'yellow', 'black']


# REPLACE WITH MORE ITEMS THAN REMOVED
nums = [10, 20, 30]
nums[1:2] = [40, 50]
print(nums)
# Output: [10, 40, 50, 30]


# REPLACE WITH FEWER ITEMS THAN REMOVED
marks = [60, 70, 80]
marks[1:3] = [75]
print(marks)
# Output: [60, 75]


# EXTEND LIST WITH ANOTHER LIST
team_a = ["Alice", "Bob"]
team_b = ["Charlie", "David"]
team_a.extend(team_b)
print(team_a)
# Output: ['Alice', 'Bob', 'Charlie', 'David']


# EXTEND LIST WITH ANY ITERABLE (TUPLE)
numbers = [1, 2, 3]
extra = (4, 5)
numbers.extend(extra)
print(numbers)
# Output: [1, 2, 3, 4, 5]


# REMOVE ITEM WHEN DUPLICATES EXIST
items = ["pen", "book", "pen", "eraser"]
items.remove("pen")
print(items)
# Output: ['book', 'pen', 'eraser']


# POP WITH INDEX
data = ["A", "B", "C", "D"]
data.pop(1)
print(data)
# Output: ['A', 'C', 'D']


# DELETE USING del (INDEX)
values = [100, 200, 300]
del values[0]
print(values)
# Output: [200, 300]


# LOOP USING INDEX (range + len)
names = ["Tom", "Jerry", "Spike"]
for i in range(len(names)):
    print(names[i])
# Output:
# Tom
# Jerry
# Spike


# LOOP USING WHILE
i = 0
while i < len(names):
    print(names[i])
    i += 1
# Output:
# Tom
# Jerry
# Spike


# LIST COMPREHENSION AS LOOP (PRINT-ONLY)
[print(x) for x in ["Python", "Java", "C++"]]
# Output:
# Python
# Java
# C++
