# Binary search
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = sorted([int(x) for x in input("Enter sorted numbers separated by space: ").split()])
target = int(input("Enter the number to find: "))
index = binary_search(lst, target)
print(f"{target} is at index {index}" if index != -1 else "Not found")