import random
import string

def generate_password(length=12):
    """Generates a random password with the given length."""
    if length < 5:
        print("Password length should be at least 5 characters for better security.")
        return None

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters + digits + special_chars

    password = (
        random.choice(letters) +
        random.choice(digits) +
        random.choice(special_chars) +
        ''.join(random.choices(all_chars, k=length - 3))
    )

    password = ''.join(random.sample(password, len(password)))
    return password

try:
    password_length = int(input("Enter the desired password length (minimum 5): "))
    generated_password = generate_password(password_length)
    if generated_password:
        print(f"Your generated password is: {generated_password}")
except ValueError:
    print("Please enter a valid number.")
