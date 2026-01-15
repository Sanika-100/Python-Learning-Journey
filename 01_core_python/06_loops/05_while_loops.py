# WHILE LOOP EXAMPLES

count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1 2 3 4 5

# break example
num = 1
while num <= 5:
    if num == 4:
        break
    print(num)
    num += 1

# Output:
# 1 2 3

# continue example
x = 0
while x < 6:
    x += 1
    if x == 3:
        continue
    print(x)

# Output:
# 1 2 4 5 6

# else with while
y = 1
while y <= 3:
    print(y)
    y += 1
else:
    print("Loop finished")

# Output:
# 1 2 3
# Loop finished
