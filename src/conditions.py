number = 42

if number == 42:
    print("42 is the meaning of life")
elif number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

if number == 42 and number % 2 == 0:
    print("42 is the meaning of life")
    print("number is also even")

if not number == 42:
    print("Number is not 42")