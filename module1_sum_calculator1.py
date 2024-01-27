def calculate_sum(a, b):
    """Calculate and return the sum of two numbers.

    Arguments used by me:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b


def main():
    """Main function to execute my program"""
    # Taking user inputs as desired in assignment
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Calculating the sum
    result = calculate_sum(num1, num2)

    # Printing the inputs and output
    print(f"The sum of {num1} and {num2} is {result}")


if __name__ == "__main__":
    main()
