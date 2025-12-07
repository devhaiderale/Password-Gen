import random
import string
from collections import Counter

def generate_secure_password(length=20):
    min_count = 5  # Minimum count for each character typ
    min_total = min_count * 4  # Total minimum characters needed
    
    if length < min_total:
        raise ValueError(f"Password length must be at least {min_total} characters to meet minimum requirements")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Initialize with minimum required characters of each type
    password = (
        [random.choice(lowercase) for _ in range(min_count)] +
        [random.choice(uppercase) for _ in range(min_count)] +
        [random.choice(digits) for _ in range(min_count)] +
        [random.choice(symbols) for _ in range(min_count)]
    )
    
    # Define all character types
    all_chars = [lowercase, uppercase, digits, symbols]
    char_types = list(range(4))  # [0, 1, 2, 3] representing each type
    
    # Fill the remaining length with random characters
    while len(password) < length:
        # Get the type of the last character
        if len(password) > 0:
            last_char = password[-1]
            last_type = (
                0 if last_char in lowercase else
                1 if last_char in uppercase else
                2 if last_char in digits else
                3
            )
            # Remove the last type from available choices
            available_types = [t for t in char_types if t != last_type]
        else:
            available_types = char_types
            
        # Choose a random type from available types
        current_type = random.choice(available_types)
        password.append(random.choice(all_chars[current_type]))
    
    # Shuffle while maintaining the no-consecutive-type rule
    while True:
        random.shuffle(password)
        valid = True
        
        # Check if the shuffled password maintains the rule
        for i in range(1, len(password)):
            prev_char = password[i-1]
            curr_char = password[i]
            
            prev_type = (
                0 if prev_char in lowercase else
                1 if prev_char in uppercase else
                2 if prev_char in digits else
                3
            )
            curr_type = (
                0 if curr_char in lowercase else
                1 if curr_char in uppercase else
                2 if curr_char in digits else
                3
            )
            
            if prev_type == curr_type:
                valid = False
                break
        
        if valid:
            break
    
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    try:
        # Generate and print 3 different passwords
        for i in range(3):
            password = generate_secure_password()
            print(f"Generated Password {i+1}: {password}")
    except ValueError as e:
        print(f"Error: {e}")

