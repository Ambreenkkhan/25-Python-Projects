import random  
import time    

# Define the main guessing function
def guess(x):
    # Display a welcome message
    print("\n🎲 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {x}. Can you guess it? 🤔")
    time.sleep(1)  # Pause for 1 second for dramatic effect

    # Generate a random number between 1 and x
    number_to_guess = random.randint(1, x)

    # Initialize the user's guess and attempt counter
    user_guess = 0
    attempts = 0

    # Repeat until the user guesses the correct number
    while user_guess != number_to_guess:
        try:
            # Take input from the user and convert it to an integer
            user_guess = int(input(f"\n Enter your guess (1 to {x}): "))
            attempts += 1  # Increment the number of attempts

            # Give feedback if the guess is too low
            if user_guess < number_to_guess:
                print("📉 Too low! Try a higher number.")
            # Give feedback if the guess is too high
            elif user_guess > number_to_guess:
                print("📈 Too high! Try a lower number.")
        except ValueError:
            # Handle non-integer input
            print("❌ Please enter a valid number!")

    # Congratulate the user when the correct number is guessed
    print(f"\n🎉 Woohoo! You guessed it right — the number was {number_to_guess}!")
    print(f"✅ You cracked it in {attempts} tries, impressive!\n")

guess(10)
