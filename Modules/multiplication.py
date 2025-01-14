def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

if __name__ == "__main__":
    num1 = float(input("Enter the first number for multiplication: "))
    num2 = float(input("Enter the second number for multiplication: "))
    print(f"The product of {num1} and {num2} is: {multiply(num1, num2)}")