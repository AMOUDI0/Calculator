# Function to calculate percentage
def calculate_percentage(total_value, percentage):
    return (percentage / 100) * total_value

# Example usage for percentage of a value
def example_usage():
    total = 200  # Example total value
    percent = 15  # Example percentage to calculate (15%)

    result = calculate_percentage(total, percent)
    print(f"{percent}% of {total} is {result}")

# Example for calculating percentage of a given amount
def calculate_percentage_value(amount, percent):
    percentage_value = (amount * percent) / 100
    print(f"{percent}% of {amount} is {percentage_value}")

# Example usage
amount = 200  # Example amount
percent = 25  # Example percentage
print(calculate_percentage(amount, percent))  # Output: 125
