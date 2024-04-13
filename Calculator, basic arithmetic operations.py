# Define a class called Calculator to perform basic arithmetic operations
class Calculator:

    # Define a method for addition that takes two arguments and returns their sum
    def add(self, x, y):
        return x + y

    # Define a method for subtraction that takes two arguments and returns their difference
    def subtract(self, x, y):
        return x - y

    # Define a method for multiplication that takes two arguments and returns their product
    def multiply(self, x, y):
        return x*y

    # Define a method for division that takes two arguments and returns the result if the denominator is not zero,
    # or an error message if the denominator is zero
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            print("Cannot divide by zero.")

# Example usage
# Create an instance of the Calculator class
calculator = Calculator()

# Perform addition and print the result
sum = calculator.add(8,4)
print(sum)

# Perform subtraction and print the result
subtraction = calculator.subtract(9,2)
print(subtraction)

# Perform multiplication and print the result
multiplication = calculator.multiply(4,5)
print(multiplication)

# Perform division and print the result
division = calculator.divide(15,5)
print(division)

# Attempt to divide by zero
division_by_zero = calculator.divide(8,0)
print(division_by_zero)

