import addition
import subtraction
import multiplication
import division
import root  # New module for square root
import Percentage  # New module for percentage


def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Percentage")

    choice = int(input("Enter your choice (1/2/3/4/5/6): "))

    # Handle operations requiring one or two inputs
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print(f"The result is: {addition.add(num1, num2)}")
        elif choice == 2:
            print(f"The result is: {subtraction.subtract(num1, num2)}")
        elif choice == 3:
            print(f"The result is: {multiplication.multiply(num1, num2)}")
        elif choice == 4:
            if num2 != 0:
                print(f"The result is: {division.divide(num1, num2)}")
            else:
                print("Error: Division by zero is not allowed.")
    elif choice == 5:
        num = float(input("Enter the number for square root: "))
        print(f"The result is: {root.sqrt(num)}")
    elif choice == 6:
        num1 = float(input("Enter the total: "))
        num2 = float(input("Enter the percentage: "))
        print(f"The result is: {Percentage.calculate_percentage(num1, num2)}")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    calculator()
