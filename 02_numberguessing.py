import random

secretnum = random.randint(1, 10)
attempts = 4

while attempts > 0:
    guess = int(input(f"\nGuess a number ({attempts} left): "))

    if guess == secretnum:
        print(" You guessed the number!")
        break
    elif guess < secretnum:
        print(" Guess higher! Try again.")
    else:
        print("Guess lower! Try again.")

    attempts -= 1

    if attempts == 0:
        print(f"\n💀 Game over! The number was {secretnum}")
