# DICTIONARY METHODS

keys = ["name", "age", "city"]
default_data = dict.fromkeys(keys, "Not Assigned")
print(default_data)

info = {"name": "Amit", "age": 25}

print(info.setdefault("city", "Mumbai"))
print(info)

print(info.keys())
print(info.values())
print(info.items())

info.clear()
print(info)
# Output
# python 04_dict_methods.py
# {'name': 'Not Assigned', 'age': 'Not Assigned', 'city': 'Not Assigned'}
# Mumbai
# {'name': 'Amit', 'age': 25, 'city': 'Mumbai'}
# dict_keys(['name', 'age', 'city'])
# dict_values(['Amit', 25, 'Mumbai'])
# dict_items([('name', 'Amit'), ('age', 25), ('city', 'Mumbai')])
# {}

