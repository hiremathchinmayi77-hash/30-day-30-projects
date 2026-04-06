import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))
upper = input("Include uppercase? (y/n): ") == 'y'
digits = input("Include digits? (y/n): ") == 'y'
symbols = input("Include symbols? (y/n): ") == 'y'

password = generate_password(length, upper, digits, symbols)

print("\nGenerated Password:", password)