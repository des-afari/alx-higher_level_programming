!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        if i > a:
            raise ValueError("i value is greater than a, which is not allowed")
        else:
            try:
                result += (a ** b) / i
            except ZeroDivisionError:
                raise ZeroDivisionError("Cannot divide by zero")
    return result
