# Compute the sum of digits of a number
num = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in num if digit.isdigit())
print(f"Sum of digits: {digit_sum}")