# PYTHON OPERATORS
# Operators are used to perform operations on values and variables


# ARITHMETIC OPERATORS
a = 15
b = 4

print(a + b)
# Output: 19

print(a - b)
# Output: 11

print(a * b)
# Output: 60

print(a / b)
# Output: 3.75

print(a % b)
# Output: 3


# ASSIGNMENT OPERATORS
x = 10
x += 5
print(x)
# Output: 15

x *= 2
print(x)
# Output: 30


# COMPARISON OPERATORS
m = 20
n = 25

print(m > n)
# Output: False

print(m <= n)
# Output: True

print(m == n)
# Output: False


# LOGICAL OPERATORS
is_logged_in = True
is_admin = False

print(is_logged_in and is_admin)
# Output: False

print(is_logged_in or is_admin)
# Output: True

print(not is_logged_in)
# Output: False


# IDENTITY OPERATORS
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
# Output: True

print(a is c)
# Output: False

print(a is not c)
# Output: True


# MEMBERSHIP OPERATORS
languages = ["Python", "Java", "C++"]

print("Python" in languages)
# Output: True

print("Ruby" not in languages)
# Output: True


# BITWISE OPERATORS
p = 6   # 110
q = 3   # 011

print(p & q)
# Output: 2

print(p | q)
# Output: 7

print(p ^ q)
# Output: 5


# OPERATOR PRECEDENCE
result = 10 + 5 * 2
print(result)
# Output: 20
