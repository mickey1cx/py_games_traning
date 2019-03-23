# python 3.7

import random

guessTaken = 0

name = input('name, please: ')
numberRange = int(input(name + ', select number range: 1 - '))
winNumber = random.randint(1, numberRange)

win = False
while not win:
    currentNumber = int(input('your number: '))
    win = currentNumber == winNumber
    guessTaken += 1
    if not win:
        print('greater') if currentNumber > winNumber else print('lesser')

print('Congratulations ' + name + ', guess taken ' + str(guessTaken))
