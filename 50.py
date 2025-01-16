# Find LCM using GCD
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a, b = map(int, input("Enter two numbers: ").split())
print(f"LCM of {a} and {b} is {lcm(a, b)}")