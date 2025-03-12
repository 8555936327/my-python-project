# main.py

def add(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts b from a and returns the result.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    """
    return a * b

def divide(a, b):
    """
    Divides a by b and returns the result.
    Raises a ZeroDivisionError if b is 0.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Simple Math Operations")
    print(f"Addition: 5 + 3 = {add(5, 3)}")
    print(f"Subtraction: 5 - 3 = {subtract(5, 3)}")
    print(f"Multiplication: 5 * 3 = {multiply(5, 3)}")
    print(f"Division: 6 / 2 = {divide(6, 2)}")
