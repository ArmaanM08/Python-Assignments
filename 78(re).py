import re

def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

# Example Usage
text = "Emails: john.doe@example.com, alice@company.org. Invalid: user@domain, test@com."
print(extract_emails(text))