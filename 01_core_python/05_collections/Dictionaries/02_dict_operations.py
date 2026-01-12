# DICTIONARY OPERATIONS

employee = {
    "id": 101,
    "role": "Developer",
    "salary": 50000
}

# Change value
employee["salary"] = 60000
print(employee)

# Update value
employee.update({"role": "Senior Developer"})
print(employee)

# Add item
employee["location"] = "Remote"
print(employee)

# Remove items
employee.pop("id")
print(employee)

employee.popitem()
print(employee)

# Loop keys
for key in employee:
    print(key)

# Loop values
for value in employee.values():
    print(value)

# Loop keys & values
for k, v in employee.items():
    print(k, v)

# Copy dictionary
copy_emp = employee.copy()
print(copy_emp)

#Output
# {'id': 101, 'role': 'Developer', 'salary': 60000}
# {'id': 101, 'role': 'Senior Developer', 'salary': 60000}
# {'id': 101, 'role': 'Senior Developer', 'salary': 60000, 'location': 'Remote'}
# {'role': 'Senior Developer', 'salary': 60000, 'location': 'Remote'}
# {'role': 'Senior Developer', 'salary': 60000}
# role
# salary
# Senior Developer
# 60000
# role Senior Developer
# salary 60000
# {'role': 'Senior Developer', 'salary': 60000}
