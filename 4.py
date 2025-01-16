# Prompt user for two numbers and display all operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2 if num2 != 0 else 'Division by zero not allowed'}")