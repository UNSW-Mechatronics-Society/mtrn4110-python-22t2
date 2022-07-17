base = "Hi from mtrnsoc"

base_as_list = base.split(" ")
print(base_as_list)
# ['Hi', 'from', 'mtrnsoc']

print(base[0])
# H (first character)
print(base[-3])
# s (3rd last character)

# [start:stop:step]
# start: It is the index from where the slice starts. The default value is 0.
# stop: It is the index at which the slice stops.
# 		The character at this index is not included in the slice.
#       The default value is the length of the string.
# step: It specifies the number of jumps to take while going from start to stop.
#       It takes the default value of 1.

print(base[3:6:1])
# fro
