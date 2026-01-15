# FOR LOOP EXAMPLES

subjects = ["Math", "Physics", "Chemistry"]

for sub in subjects:
    print(sub)

# Output:
# Math
# Physics
# Chemistry

# Loop through string
for ch in "Python":
    print(ch)

# break example
for n in range(1, 6):
    if n == 4:
        break
    print(n)

# Output:
# 1 2 3

# continue example
for n in range(1, 6):
    if n == 3:
        continue
    print(n)

# Output:
# 1 2 4 5
