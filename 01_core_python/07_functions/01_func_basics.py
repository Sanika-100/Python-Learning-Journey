# -----------------------------
# PYTHON FUNCTIONS - BASICS
# -----------------------------

# 1️⃣ Creating and Calling a Function
def greet():
    print("Hello, welcome to Python functions")

greet()

# Output:
# Hello, welcome to Python functions


# 2️⃣ Function with Return Value
def square(num):
    return num * num

result = square(6)
print(result)

# Output:
# 36


# 3️⃣ Function with Arguments
def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("Sanika", "Ganorkar"))

# Output:
# Sanika Ganorkar


# 4️⃣ Default Arguments
def country_name(country="India"):
    print("Country:", country)

country_name("Japan")
country_name()

# Output:
# Country: Japan
# Country: India
