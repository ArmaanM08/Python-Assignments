# Swap variables without using a temporary variable
a = int(input("Enter the first value (a): "))
b = int(input("Enter the second value (b): "))
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")