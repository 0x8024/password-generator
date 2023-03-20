import random
import string

def generate_password(length, include_uppercase=False, include_numbers=False, include_special_chars=False):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

# Ask the user for password preferences
length = int(input("Enter password length: "))
include_uppercase = input("Include uppercase letters? (Yes/No): ").lower() == "yes"
include_numbers = input("Include numbers? (Yes/No): ").lower() == "yes"
include_special_chars = input("Include special characters? (Yes/No): ").lower() == "yes"

# Generate the password and display it
password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
print("The generated password is:", password)
