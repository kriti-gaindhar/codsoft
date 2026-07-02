import random
import string
import math


def calculate_strength(password):
    """
    Calculates password strength based on entropy.
    Entropy = L * log2(R), where L is length and R is the pool size.
    """
    length = len(password)
    charset_size = 0
    
    if any(c.islower() for c in password): charset_size += 26
    if any(c.isupper() for c in password): charset_size += 26
    if any(c.isdigit() for c in password): charset_size += 10
    if any(c in string.punctuation for c in password): charset_size += 32
    
    if charset_size == 0: return "Very Weak"
    
    entropy = length * math.log2(charset_size)
    
    if entropy < 50: return "Weak"
    elif entropy < 80: return "Moderate"
    elif entropy < 120: return "Strong"
    else: return "Very Strong"


def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    """Generates a password based on user criteria."""
    char_pool = ""
    if use_upper: char_pool += string.ascii_uppercase
    if use_lower: char_pool += string.ascii_lowercase
    if use_numbers: char_pool += string.digits
    if use_symbols: char_pool += string.punctuation
    
    if not char_pool:
        return None
    
    # Ensure at least one of each selected type is included
    password = []
    if use_upper: password.append(random.choice(string.ascii_uppercase))
    if use_lower: password.append(random.choice(string.ascii_lowercase))
    if use_numbers: password.append(random.choice(string.digits))
    if use_symbols: password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password
    remaining_length = max(0, length - len(password))
    for _ in range(remaining_length):
        password.append(random.choice(char_pool))
        
    random.shuffle(password)
    return "".join(password)


def main():
    print("--- Secure Python Password Generator ---")
    
    try:
        length = int(input("Enter desired length: "))
        u = input("Include Uppercase? (y/n): ").lower() == 'y'
        l = input("Include Lowercase? (y/n): ").lower() == 'y'
        n = input("Include Numbers? (y/n): ").lower() == 'y'
        s = input("Include Symbols? (y/n): ").lower() == 'y'
        
        password = generate_password(length, u, l, n, s)
        
        if password:
            strength = calculate_strength(password)
            print(f"\nGenerated Password: {password}")
            print(f"Strength Indicator: {strength}")
        else:
            print("\nError: Please select at least one character type.")
            
    except ValueError:
        print("Invalid input. Please enter a number for length.")


if __name__ == "__main__":
    main()