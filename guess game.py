import random
# Generate a random number between 1 and 99
number = random.randint(1, 99)
# Get the user's guess
guess = int(input("Guess a number between 1 and 99: "))
# Check if the guess is correct
while guess != number:
    # If the guess is too high, tell the user to guess lower
    if guess > number:
        print("Your guess is too high. Guess lower:")
        guess = int(input("Guess a number between 1 and 99: "))
    # If the guess is too low, tell the user to guess higher
    else:
        print("Your guess is too low. Guess higher:")
        guess = int(input("Guess a number between 1 and 99: "))
# If the guess is correct, tell the user they won
print("You guessed the correct number!")
