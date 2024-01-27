def calculate_sum(a, b):
    """Calculate and return the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b

def calculate_product(a, b):
    """Calculate and return the product of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b

def main():
    """Main function to execute the program."""
    # Taking user inputs
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Calculating the sum and product
    sum_result = calculate_sum(num1, num2)
    product_result = calculate_product(num1, num2)

    # Printing the inputs and results
    print(f"The sum of {num1} and {num2} is {sum_result}")
    print(f"The product of {num1} and {num2} is {product_result}")

if __name__ == "__main__":
    main()
