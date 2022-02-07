# Guess the Number game

import random

guessCount = 0

print("Hello! What is your name? ")
myName = input()

number = random.randint(1,20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20")

for i in range(6):
    print("Take a guess. ")  
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low. ")
        guessCount += 1

    if guess > number:
        print("Your guess is too high. ")
        guessCount += 1

    if guess == number:
        break

if guess == number:
    guessCount = str(guessCount + 1)
    print("Good job, " + myName + " You guessed my number in " + guessCount + " guesses!")

if guess != number:
    number = str(number)
    print("Nope, the number I was thinking of was " + number + ".")