# Set Basics

Skills = {"Python", "Java", "Python", "C++"}
print(Skills)

print(len(Skills))

data = {"C#", 23,True}
print(data)
#unordered set

#type
print(type(data))

#Using set as constructor
nums = set({1,4,7,8,90,24})
print(nums)

#Membership
print("Java" in Skills)
print("C++" not in Skills)

#Loops
for items in Skills:
    print(items)

# Output:
# {'Python', 'C++', 'Java'}
# 3
# {'C#', True, 23}
# <class 'set'>
# {1, 4, 7, 8, 24, 90}
# True
# False
# Python
# C++
# Java
