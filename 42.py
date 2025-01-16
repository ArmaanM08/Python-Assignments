# Find the second largest element
nums = sorted(set([int(x) for x in input("Enter numbers separated by space: ").split()]))
print(f"Second largest element: {nums[-2]}")