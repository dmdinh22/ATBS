# This is a number guessing game
# This is a guess the number game.
import random

secret_num = random.randint(1, 20) # set number to guess to random int bt 1 & 20
print('I am thinking of a number between 1 and 20.')

# ask playet to guess up to 6 times
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input()) # set user input to guess var

    if guess < secret_num:
        print('Your guess is too low.')
    elif guess > secret_num:
        print('Your guess is too high.')
    else:
        break    # this condition is the correct guess

if guess == secret_num: # if user guessed right
    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_num))
