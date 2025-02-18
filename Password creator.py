import random
import string

def create_password(size=12, include_special=True):
    # Character categories
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    specials = string.punctuation if include_special else ''

    # Combine all characters
    all_characters = lower + upper + numbers + specials

    # Ensure the password has at least one character from each category
    if size < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Start the password with one character from each category
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(numbers),
        random.choice(specials) if include_special else random.choice(numbers)
    ]

    # Fill the rest of the password length with random characters
    password_chars += random.choices(all_characters, k=size - len(password_chars))

    # Shuffle the characters to ensure randomness
    random.shuffle(password_chars)

    # Convert the list of characters into a string
    return ''.join(password_chars)

# Main execution
if _name_ == "_main_":
    desired_length = int(input("Specify the password length (minimum 4): "))
    special_characters = input("Would you like to include special characters? (y/n): ").strip().lower() == 'y'
    
    generated_password = create_password(size=desired_length, include_special=special_characters)
    print(f"Your generated password is: {generated_password}")