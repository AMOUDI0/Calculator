def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

if __name__ == "__main__":
    num1 = float(input("Enter the first number for subtraction: "))
    num2 = float(input("Enter the second number for subtraction: "))
    print(f"The difference when {num2} is subtracted from {num1} is: {subtract(num1, num2)}")
