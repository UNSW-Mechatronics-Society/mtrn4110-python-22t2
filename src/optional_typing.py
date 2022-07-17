number: int = 42
number = "hello" # should error

def add_numbers(a: int, b: int) -> int:
    return a + b

some_string: str = "Hello World"
some_string = add_numbers(1, 2) # should error