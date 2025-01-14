import addition
import subtraction
import multiplication
import division

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice (1/2/3/4): "))

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        print(f"The result is: {addition.add(num1, num2)}")
    elif choice == 2:
        print(f"The result is: {subtraction.subtract(num1, num2)}")
    elif choice == 3:
        print(f"The result is: {multiplication.multiply(num1, num2)}")
    elif choice == 4:
        print(f"The result is: {division.divide(num1, num2)}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    calculator()