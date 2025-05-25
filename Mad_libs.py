import random
import time

print("\n🤣 === Welcome to the Silly Mad Libs Game! === 🤣\n")

# Only 2 inputs from user
animal = input(" Enter an animal: ")
weird_thing = input("🧠 Enter a weird object (e.g. slipper, toothpaste): ")

# Random funny verbs and places
verbs = ["danced", "sneezed", "teleported", "screamed", "ate a laptop"]
places = ["on the moon", "in the bathroom", "inside a fridge", "at the zoo", "under your bed"]

# Randomly choose one from each list
verb = random.choice(verbs)
place = random.choice(places)

# Create a funny story
story = (
    f"\nOne day, a {animal} found a magical {weird_thing}.\n"
    f"It suddenly {verb} {place} and turned into a toy. \n"
    f"The world was never the same again. 😂\n"
)

# Add suspense
print("\n🧠 Processing your madness...\n")
time.sleep(1.5)

print(story)
print("🎬 The End (or is it...?) 😜\n")
