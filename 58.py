# Find and replace a word in a file
file_path = input("Enter the file path: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

with open(file_path, 'r') as file:
    content = file.read()

content = content.replace(old_word, new_word)

with open(file_path, 'w') as file:
    file.write(content)

print(f"Replaced '{old_word}' with '{new_word}' in {file_path}")