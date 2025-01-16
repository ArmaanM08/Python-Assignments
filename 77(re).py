import re

def validate_phone_numbers(text):
    pattern = r"\b\d{10}\b"  # Simple pattern for 10-digit numbers
    return re.findall(pattern, text)

# Example Usage
text = "Contact: 1234567890, 9876543210. Invalid: 12345, 12345678901."
print(validate_phone_numbers(text))