import time
import sys
import os

# Beep sound for end alert
def beep():
    try:
        if os.name == 'nt':
            import winsound
            winsound.Beep(1000, 500)
        else:
            print('\a', end='')
    except:
        pass

# Display progress bar with time left
def progress_bar(current, total, bar_length=30):
    percent = current / total
    filled_length = int(bar_length * percent)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\rTimer: [{bar}] {total - current}s remaining ')
    sys.stdout.flush()

# Main countdown function
def countdown(t):
    print(f"\n⏳ Countdown started for {t} seconds...\n")
    total_time = t
    for elapsed in range(total_time + 1):
        progress_bar(elapsed, total_time)
        time.sleep(1)
    print('\n \r ⏱️  Time’s up!                          ')
    beep()

# Input with validation
try:
    t = int(input("⏱️  Enter countdown time in seconds: "))
    if t <= 0:
        print("⚠️ Please enter a positive number.")
    else:
        countdown(t)
except ValueError:
    print("⚠️ Invalid input. Please enter a number.")
