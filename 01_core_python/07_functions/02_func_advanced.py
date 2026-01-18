# -----------------------------
# PYTHON FUNCTIONS - ADVANCED
# -----------------------------

# 5️⃣ Arbitrary Arguments (*args)
def add_numbers(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add_numbers(2, 4, 6))
print(add_numbers(1, 2, 3, 4))

# Output:
# 12
# 10


# 6️⃣ Arbitrary Keyword Arguments (**kwargs)
def student_details(**info):
    for key, value in info.items():
        print(key, ":", value)

student_details(name="Sanika", branch="IT", year=2025)

# Output:
# name : Sanika
# branch : IT
# year : 2025


# 7️⃣ Local vs Global Scope
count = 10

def update_count():
    global count
    count += 5

update_count()
print(count)

# Output:
# 15


# 8️⃣ Lambda Function
multiply = lambda a, b: a * b
print(multiply(4, 5))

# Output:
# 20
