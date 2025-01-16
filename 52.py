# Write user input to a file
content = input("Enter text to write to the file: ")
file_path = input("Enter the file name: ")
with open(file_path, 'w') as file:
    file.write(content)
print(f"Content written to {file_path}")