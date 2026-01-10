# LIST COMPREHENSION AND LIST METHODS


# BASIC LIST COMPREHENSION
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
# Output: [2, 4, 6]


# LIST COMPREHENSION WITH RANGE
squares = [x * x for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]


# LIST COMPREHENSION WITH IF-ELSE
status = ["Pass" if m >= 40 else "Fail" for m in [35, 60, 45, 30]]
print(status)
# Output: ['Fail', 'Pass', 'Pass', 'Fail']


# MODIFYING OUTPUT USING EXPRESSION
names = ["python", "java", "c++"]
upper_names = [name.upper() for name in names]
print(upper_names)
# Output: ['PYTHON', 'JAVA', 'C++']


# SORTING LIST (ALPHANUMERIC)
scores = [88, 45, 92, 67, 55]
scores.sort()
print(scores)
# Output: [45, 55, 67, 88, 92]


# SORT DESCENDING
scores.sort(reverse=True)
print(scores)
# Output: [92, 88, 67, 55, 45]


# CUSTOM SORT USING KEY
def distance_from_50(n):
    return abs(n - 50)

values = [10, 50, 70, 40]
values.sort(key=distance_from_50)
print(values)
# Output: [50, 40, 70, 10]


# CASE INSENSITIVE SORT
languages = ["Python", "java", "C", "Ruby"]
languages.sort(key=str.lower)
print(languages)
# Output: ['C', 'java', 'Python', 'Ruby']


# REVERSE LIST ORDER
languages.reverse()
print(languages)
# Output: ['Ruby', 'Python', 'java', 'C']


# COPYING A LIST
original = [100, 200, 300]
copy1 = original.copy()
print(copy1)
# Output: [100, 200, 300]

copy2 = list(original)
print(copy2)
# Output: [100, 200, 300]

copy3 = original[:]
print(copy3)
# Output: [100, 200, 300]


# JOINING LISTS USING +
a = ["A", "B"]
b = [1, 2]
combined = a + b
print(combined)
# Output: ['A', 'B', 1, 2]


# JOINING LISTS USING EXTEND
a.extend(b)
print(a)
# Output: ['A', 'B', 1, 2]


# USING LIST METHODS
data = [5, 3, 5, 2]

print(data.count(5))
# Output: 2

data.remove(3)
print(data)
# Output: [5, 5, 2]

data.pop()
print(data)
# Output: [5, 5]

data.clear()
print(data)
# Output: []
