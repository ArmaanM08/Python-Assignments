# Print Fibonacci sequence up to n terms
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Sequence:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()