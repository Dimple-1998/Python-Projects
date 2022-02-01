#shuffle game to pick the correct can having the red ball
from random import shuffle
#shuffle the cans
def shuffle_can(mylist):
    shuffle(mylist)
    return mylist
#make the player guess it
def player_guess():
    #initialize the guess
    guess = ''
    #get the guess till it is guesses three cans only
    while guess not in ['0', '1', '2']:
        guess = input('Pick a guess from 0,1 or 2: ')
    return int(guess)
#check the players guess
def check_guess(mylist,guess):
    if mylist[guess] == 0:
        print('Bingo!, You win')
    else:
        print('Wrong guess!, game over')
#intial list
mylist = ['0', ' ', ' ']
#shuffled ball in the can
new_list = shuffle_can(mylist)
#player guess
guess = player_guess()
#check the guess
check_guess(new_list,guess)
print('The correct ball was here')
print(new_list)