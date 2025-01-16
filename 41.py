# Remove duplicates from a list
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique_nums = list(set(nums))
print(f"List without duplicates: {unique_nums}")