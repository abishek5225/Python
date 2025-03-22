import random

secretnum = random.randint(1,5)

guess = int(input("Guess a number between 1 and 10:"))

if(guess == secretnum){
    print("You guessed the number!")
}
