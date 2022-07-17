userData = {
    'name' : 'Janice',
    'age' : 129,
    'height' : '180cm'
}

print(userData.get("name"))
# janice

print(userData.get("zID", None))
# None (similar to null)