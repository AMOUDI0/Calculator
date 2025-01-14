def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    num1 = float(input("Enter the first number for addition: "))
    num2 = float(input("Enter the second number for addition: "))
    print(f"The sum of {num1} and {num2} is: {add(num1, num2)}")
