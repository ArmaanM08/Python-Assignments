# Compute power without using built-in functions
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
for _ in range(abs(exponent)):
    result *= base
if exponent < 0:
    result = 1 / result
print(f"{base} to the power of {exponent} is {result}")