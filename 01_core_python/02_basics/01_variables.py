# Variables in Python

name = "Sanika"
age = 22
height = 5.4
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# Reassigning values
age = 23
print(age)

# Variable naming examples
_valid_name = "Allowed"
name123 = "Allowed"

# Multiple variable assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Assign same value to multiple variables
a = b = c = 100
print(a, b, c)

# Dynamic typing example
value = 10
print(value, type(value))

value = "Ten"
print(value, type(value))


# -------------------- OUTPUT --------------------
# Sanika
# 22
# 5.4
# True
# 23
# 10 20 30
# 100 100 100
# 10 <class 'int'>
# Ten <class 'str'>

# Global Variable Example

course = "Python"

def show_course():
    print(course)

show_course()


# Using global keyword

count = 10

def update_count():
    global count
    count = count + 5

update_count()
print(count)


# -------------------- OUTPUT --------------------
# Python
# 15

