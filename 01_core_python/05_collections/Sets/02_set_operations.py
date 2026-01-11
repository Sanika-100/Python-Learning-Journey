# SET OPERATIONS

# Add elements
colors = {"Red", "Blue"}
colors.add("Green")
print(colors)

colors.update(["Yellow", "Black"])
print(colors)

# Remove elements
colors.remove("Red")
print(colors)

colors.discard("Pink")  # no error
print(colors)

removed = colors.pop()
print("Removed:", removed)
print(colors)

# Join sets
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a | b)

# Intersection
print(a.intersection(b))
print(a & b)

# Difference
print(a.difference(b))
print(a - b)

# Symmetric difference
print(a.symmetric_difference(b))
print(a ^ b)

# Update operations
x = {10, 20, 30}
y = {20, 40}

x.intersection_update(y)
print(x)

# Frozenset
f = frozenset([1, 2, 3])
print(f)
print(type(f))

# Frozenset operations
print(f.union({4, 5}))
print(f.intersection({2, 3, 6}))
