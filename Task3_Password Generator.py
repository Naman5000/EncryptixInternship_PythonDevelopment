import random
import string

def generate_password(length):
    if length < 1:
        return "Error! Password length should be at least 1."
    
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_characters = lower + upper + digits + special
    
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the remaining length of the password
    if length > 4:
        password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to ensure random order
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
