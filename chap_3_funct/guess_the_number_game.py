import random

# generate a random int
secretNumber = random.randint(1, 20)

print ('I am thinking of a number between 1 and 20.')

# the player has 6 chances to guess the correct number 
for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # this gets us out of the flow if the user is correct. 
    
if guess == secretNumber:
    print('Well done! you guessed the number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))