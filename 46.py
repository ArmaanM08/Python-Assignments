# Count frequency of elements in a list
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
frequency = {}
for num in nums:
    frequency[num] = frequency.get(num, 0) + 1
print(f"Frequency: {frequency}")