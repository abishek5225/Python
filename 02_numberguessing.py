import random

secretnum = random.randint(1,10)
attempts = 3

while attempts > 0:
     guess = int(input("\nGuess a number ({attempts} left):"))

if(guess == secretnum):
    print("You guessed the number!")
    break

    elif guess < secretnum:
        print("guess higher! Try again.")
else:
    print("Guess lower! Try again.")
