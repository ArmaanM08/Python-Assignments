# Read and print file contents
file_path = input("Enter the file path: ")
with open(file_path, 'r') as file:
    print(file.read())