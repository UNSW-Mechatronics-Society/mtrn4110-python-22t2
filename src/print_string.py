name = "Giraffe"
age = 18
height = 2048.11  # mm

# Different ways of printing the same code
# Giraffe, 18, 2048.11
print(name + ", " + str(age) + ', ' + str(height))  # string concatenation
print(name, age, height, sep=', ')
print(f"{name}, {age}, {height}")  # f-strings
