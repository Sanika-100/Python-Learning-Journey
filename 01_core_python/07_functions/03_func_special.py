# -----------------------------
# PYTHON FUNCTIONS - SPECIAL TOPICS
# -----------------------------

# 9️⃣ Recursion (Factorial)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Output:
# 120


# 🔟 Generators
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for value in count_up_to(4):
    print(value)

# Output:
# 1
# 2
# 3
# 4


# 1️⃣1️⃣ Decorators
def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def message():
    return "learning python functions"

print(message())

# Output:
# LEARNING PYTHON FUNCTIONS
