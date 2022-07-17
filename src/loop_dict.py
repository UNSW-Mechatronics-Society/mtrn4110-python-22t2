userData = {
    'name' : 'Janice',
    'age' : 129,
    'height' : '180cm'
}

print(userData.items())
# dict_items([('name', 'Janice'), ('age', 129), ('height', '180cm')])
# List of tuples that we can destructure in the loop

for key, value in userData.items():
    print(f"{key}: {value}")

# name: Janice
# age: 129
# height: 180cm