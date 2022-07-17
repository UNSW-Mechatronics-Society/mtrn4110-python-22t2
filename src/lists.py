names = ["Tanvee", "Alvin", "Juliet"]
names.append("Brandon")
print(names) # list is now ['Tanvee', 'Alvin', 'Juliet', 'Brandon']

for name in names:
    print(name)

# This prints
# Tanvee
# Alvin
# Juliet
# Brandon

# Concatenating lists
names += ["Kyra", "Iniyan"]

# Printing using indexes, like an array in c++
for i in range(0, len(names)):
    print(names[i])

# Indexing is always dangerous, but if you need
# to know the index, this would be the better way

for index, name in enumerate(names):
    print(f"{index} {name}")

# 0 Tanvee
# 1 Alvin
# 2 Juliet
# 3 Brandon
# 4 Kyra
# 5 Iniyan