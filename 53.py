# Copy contents of one file to another
source = input("Enter the source file path: ")
destination = input("Enter the destination file path: ")
with open(source, 'r') as src, open(destination, 'w') as dest:
    dest.write(src.read())
print(f"Copied content from {source} to {destination}")