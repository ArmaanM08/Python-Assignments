# Bubble sort implementation
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
n = len(nums)
for i in range(n):
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(f"Sorted List: {nums}")