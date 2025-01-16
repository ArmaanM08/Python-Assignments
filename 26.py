# Check if a substring is present in a string
s = input("Enter the main string: ")
sub = input("Enter the substring: ")
if sub in s:
    print(f"'{sub}' is present in the string.")
else:
    print(f"'{sub}' is not present in the string.")