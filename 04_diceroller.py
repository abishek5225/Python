import random

print("Welcome to Dice Roller")

while True:
    input("Press Enter to roll the dice..")

    dice=random.randint(1,6)
    print(f"You rolled:{dice}")

    choice = input("Roll again?(yes/no)").lower()

    if choice != "yes":
        print("Thanks for playing")