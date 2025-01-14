def divide(a, b):
    """Returns the quotient of two numbers. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

if __name__ == "__main__":
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = divide(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result}")