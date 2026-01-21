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

#Return Statement
#Square of a number.

print('--------')
def square(a =7):  #return a * a
    return a ** 2


result = square(20)
print(result)


#Count Vowels and consonants
def count(userinput):
    vowelsare = "AEIOUaeiou"
    cntv = 0
    cntc = 0

    for eachchar in userinput:
        if(eachchar.isalpha()):
            if(eachchar in vowelsare):
                cntv += 1
            else:
                cntc += 1

    return cntv, cntc
vowels, conso =  count("Sanik")
print(vowels, conso)


# Output:
# Country: Japan
# Country: India
# --------
# 400
# 2 3
