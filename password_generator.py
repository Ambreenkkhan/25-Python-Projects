import random
import string  # ✅ Cleaner way to get letters and digits

def generate_password(length, use_special_chars=True):
    """
    Generate a random password with the given length.
    Includes special characters if 'use_special_chars' is True.
    """
    #  Build character set based on user's choice
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += '!@#$%^&*'

    #  Randomly pick characters for the password
    return ''.join(random.choice(chars) for _ in range(length))


def main():
    print('\n🔐 Welcome to the "Password Generator"!\n')

    #  Ask user how many passwords to generate
    try:
        num = int(input(' How many passwords would you like to generate? '))
        length = int(input(' Enter your desired password length: '))
    except ValueError:
        print("❌ Please enter valid numbers.")
        return

    # ✅ Ask if user wants special characters
    choice = input(" Include special characters? (yes/no): ").strip().lower()
    use_special_chars = choice in ['yes', 'y']

    print('\n🧾 Your generated passwords:')
    print('-' * 30)

    #  Generate and display passwords
    for i in range(num):
        password = generate_password(length, use_special_chars)
        print(f'{i + 1}: {password}')

    print('-' * 30)
    print('✅ Done! Keep your passwords safe.')

if __name__ == '__main__':
    main()
