# Read and write JSON
import json

file_path = input("Enter the JSON file path: ")
with open(file_path, 'r') as file:
    data = json.load(file)

print(f"Original Data: {data}")

key = input("Enter the key to modify: ")
if key in data:
    value = input("Enter the new value: ")
    data[key] = value
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print("Updated the JSON file.")
else:
    print(f"Key '{key}' not found in the JSON file.")