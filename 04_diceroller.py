import random

print("Welcome to Dice Roller")

while True:
    input("Press Enter to roll the dice..")

    dice=random.randint(1,6)
    print(f"You rolled:{dice}")

    choice = input("Roll again?(y/n)").lower()

    if choice != "y":
        print("Thanks for playing")
        break