# RANGE FUNCTION

for i in range(3):
    print(i)

# Output:
# 0 1 2

for i in range(2, 6):
    print(i)

# Output:
# 2 3 4 5

for i in range(2, 10, 2):
    print(i)

# Output:
# 2 4 6 8


# ELSE WITH FOR LOOP
for i in range(3):
    print(i)
else:
    print("For loop completed")

# Output:
# 0 1 2
# For loop completed


# NESTED LOOPS
rows = ["A", "B"]
cols = [1, 2, 3]

for r in rows:
    for c in cols:
        print(r, c)

# Output:
# A 1
# A 2
# A 3
# B 1
# B 2
# B 3

# PASS STATEMENT

for i in range(5):
    if i == 3:
        pass
    else:
        print(i)

# Output:
# 0 1 2 4

