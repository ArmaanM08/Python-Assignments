# Convert string to integer with error handling
def safe_convert(string):
    try:
        return int(string)
    except ValueError:
        print(f"Error: '{string}' is not a valid integer.")

value = input("Enter a string to convert to integer: ")
result = safe_convert(value)
if result is not None:
    print(f"Converted value: {result}")