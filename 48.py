# Recursive sum of a list
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(f"Sum of list: {recursive_sum(nums)}")