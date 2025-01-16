# Check if a number is a palindrome
num = input("Enter a number: ")
print(f"{num} is {'a palindrome' if num == num[::-1] else 'not a palindrome'}.")