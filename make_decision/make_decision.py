#! /usr/bin/env/python3

import random, time

#Show introduction
def introDisplay():
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.''')

    
#Player choose
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print("Make your move (1 or 2)")
        cave = input()
    return cave


#Check for the right decision
def checkCave(chooseCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    rightCave = random.randint(1, 2)

    if chooseCave == str(rightCave):
        print('Gives you his treasure!')
    else:
        print('Drogons ate you')


#Game run and ask play again
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    introDisplay()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Play again?')
    playAgain = input()
