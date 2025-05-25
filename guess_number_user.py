import random
import time

#  created main function for the computer guessing game
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    attempts = 0

    #  added welcome message and instructions
    print("\n🤖 Welcome to 'Number guessing game'!")
    print(f"Think of a number between 1 and {x}! 🤫")
    input("When you're ready, press Enter and I'll try to guess it!\n")

    # loop: repeat until guess is correct
    while feedback != 'c':
        attempts += 1

        # logic: generate guess within updated range
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # only one number left

        # added dramatic pause for realism
        print(f"🤖 Hmm... Let me think...")
        time.sleep(1.2)
        print(f" Is it... {guess}?")

        #  ask user for feedback
        feedback = input(" Type 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        #  validate user input
        while feedback not in ['h', 'l', 'c']:
            feedback = input("❌ Oops! Please enter 'h', 'l', or 'c': ").lower()

        #  adjust range based on feedback
        if feedback == 'h':
            print("😅 Too high? Let me lower my expectations...\n")
            high = guess - 1
        elif feedback == 'l':
            print("🔍 Too low? I'll aim higher!\n")
            low = guess + 1

    # 
    # guessed the number correctly
    print(f"\n🎉 Yay! I guessed it right — it's {guess}!")
    print(f"🧠 I cracked your mind in just {attempts} attempt(s)! 🤯\n")

# 🚀 run: execute the game with range 1–10
computer_guess(10)
