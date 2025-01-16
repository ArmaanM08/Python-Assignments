# Reverse a list in-place
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
for i in range(len(nums) // 2):
    nums[i], nums[-i - 1] = nums[-i - 1], nums[i]
print(f"Reversed List: {nums}")