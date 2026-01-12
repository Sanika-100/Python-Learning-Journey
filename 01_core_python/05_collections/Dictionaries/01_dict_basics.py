# DICTIONARY BASICS

student = {
    "name": "Sanika",
    "age": 22,
    "branch": "IT"
}

print(student)
# Output: {'name': 'Sanika', 'age': 22, 'branch': 'IT'}

# Access items
print(student["name"])
# Output: Sanika

print(student.get("age"))
# Output: 22

# Length
print(len(student))
# Output: 3

# Type
print(type(student))
# Output: <class 'dict'>

# Using dict() constructor
profile = dict(city="Pune", country="India")
print(profile)
# Output: {'city': 'Pune', 'country': 'India'}

# Duplicate key overwrite
data = {"a": 1, "a": 5}
print(data)
# Output: {'a': 5}
