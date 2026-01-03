# PYTHON BOOLEANS
# Boolean values represent True or False


# BOOLEAN EXPRESSIONS
x = 25
y = 40

print(x > y)
# Output: False

print(x == y)
# Output: False

print(x != y)
# Output: True


# BOOLEANS IN CONDITIONS
marks = 72

if marks >= 35:
    print("Student passed")
else:
    print("Student failed")
# Output: Student passed


# BOOL() FUNCTION
print(bool("Python"))
# Output: True

print(bool(0))
# Output: False

print(bool(3.14))
# Output: True


# BOOLEAN WITH VARIABLES
language = "Java"
version = 17

print(bool(language))
# Output: True

print(bool(version))
# Output: True


# VALUES THAT ARE TRUE
print(bool("AI"))
# Output: True

print(bool(101))
# Output: True

print(bool([1, 2, 3]))
# Output: True

print(bool({"name": "Sanika"}))
# Output: True


# VALUES THAT ARE FALSE
print(bool(""))
# Output: False

print(bool(0))
# Output: False

print(bool([]))
# Output: False

print(bool({}))
# Output: False

print(bool(None))
# Output: False


# FUNCTION RETURNING BOOLEAN
def is_even(num):
    return num % 2 == 0

print(is_even(10))
# Output: True

print(is_even(7))
# Output: False


# USING BOOLEAN FUNCTION IN CONDITION
if is_even(10):
    print("Even number")
else:
    print("Odd number")
# Output: Even number


# BUILT-IN FUNCTION RETURNING BOOLEAN
value = 50
print(isinstance(value, int))
# Output: True
