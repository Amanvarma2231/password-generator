import random
import string

# Function to generate a password
def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = lowercase + uppercase + digits + symbols
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    for _ in range(length - 4):
        password.append(random.choice(all_characters))
    random.shuffle(password)
    return ''.join(password)
def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8 characters): "))
            if length < 8:
                print("Password length should be at least 8 characters for security.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    password = generate_password(length)
    print(f"\nYour generated password is: {password}")
    print("\nMake sure to store this password securely and not share it with others.")
if __name__ == "__main__":
    main()
