# Count occurrences of an integer in a list
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
target = int(input("Enter the number to count: "))
count = 0
for num in nums:
    if num == target:
        count += 1
print(f"{target} appears {count} times in the list.")