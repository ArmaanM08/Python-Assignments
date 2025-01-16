# Store 5 integers in a list and print its length
nums = [int(input(f"Enter number {i+1}: ")) for i in range(5)]
print(f"List: {nums}")
print(f"Length of the list: {len(nums)}")