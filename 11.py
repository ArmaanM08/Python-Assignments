# Return the length of a string without using len()
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

input_string = input("Enter a string: ")
print(f"Length of the string: {string_length(input_string)}")