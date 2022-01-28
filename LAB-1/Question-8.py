# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random
number = random.randrange(1, 10)
guessNumber = int(input('Guess a number:'))
if guessNumber < number:
    print("You've guessed too low!")
elif guessNumber > number:
    print("You've guessed too high!")
elif guessNumber == number:
    print("You've guessed exactly right")
