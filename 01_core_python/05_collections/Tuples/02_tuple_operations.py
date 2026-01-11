#Tuple operations

#Update tuple using list conversion
colors = ("red", "Blue", "green")
to_list = list(colors) #Converted to List
to_list[2] = "Yellow"
#Converted to tuple
colors = tuple(to_list)
print(colors)

#Add item using tuple addition
colors = colors + ("Green",100)
print(colors)

#Remove item workaround
to_list = list(colors)
to_list.remove("red")
colors = tuple(to_list)
print(colors)

#Unpacking
person_info = ("Sanika G", 23, "IT depart.")
name, age, branch = person_info
print(name)
print(age)
print(branch)

#Unpacking with Asterisk
numbers = (30,40,40,60,60)
a, b, *restnos = numbers
print(a)
print(b)
print(restnos)

x, *y, restnos = numbers
print(x)
print(y)
print(restnos)

#Looping
# 1. FOR LOOP (DIRECT)
subjects = ("Maths", "Chemistry", "Physics")
for i in subjects:
    print(i)

print("=========")
#2. FOR LOOP USING INDEX
for x in range(len(subjects)):
    print(subjects[x])
print("=========")
#3.WHILE LOOP
y = 0
while y < len(subjects):
    print(subjects[y])
    y = y + 1


#Join tuples
tuple_1 =(10,30,50)
tuple_2 = (90, 70)
add_tuples = tuple_1 + tuple_2
print(add_tuples)

#Multiply tuple
multi  = tuple_2 * 2
print(multi)

#tuple methods
count_digit = (2,4,6,8,6,3,96,0.6,6)
print(count_digit.count(6))

numbers =  (100,300,400)
print(numbers.index(300))


#Output
# ('red', 'Blue', 'Yellow')
# ('red', 'Blue', 'Yellow', 'Green', 100)
# ('Blue', 'Yellow', 'Green', 100)
# Sanika G
# 23
# IT depart.
# 30
# 40
# [40, 60, 60]
# 30
# [40, 40, 60]
# 60
# Maths
# Chemistry
# Physics
# =========
# Maths
# Chemistry
# Physics
# =========
# Maths
# Chemistry
# Physics
# (10, 30, 50, 90, 70)
# (90, 70, 90, 70)
# 3
# 1











