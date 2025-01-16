import random

# Guess the number game
random_num = random.randint(1, 10)
guess = None
print("Guess a number between 1 and 10.")
while guess != random_num:
    guess = int(input("Your guess: "))
    if guess < random_num:
        print("Too low!")
    elif guess > random_num:
        print("Too high!")
print("You guessed it!")