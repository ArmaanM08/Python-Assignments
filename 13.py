# Demonstrate string slicing operations
string = input("Enter a string: ")
print(f"Original String: {string}")
print(f"Reversed String: {string[::-1]}")
print(f"Every second character: {string[::2]}")
print(f"Substring from index 2 to 5: {string[2:6]}")