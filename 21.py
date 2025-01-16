# Find minimum and maximum without using min() or max()
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
min_val = nums[0]
max_val = nums[0]
for num in nums:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
print(f"Minimum: {min_val}, Maximum: {max_val}")