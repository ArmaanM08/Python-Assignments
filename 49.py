# Find GCD using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input("Enter two numbers: ").split())
print(f"GCD of {a} and {b} is {gcd(a, b)}")