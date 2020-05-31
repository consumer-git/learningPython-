#make a rock paper scicors game
#rock > scisors >paper > rock
import random
import time

bank=['rock','paper','scisors']
cpu_randy=random.choice(bank)

counter = 0
maxguess_allowed = 3
earned=0

while counter<maxguess_allowed:

        first=input ( 'hi welcome to ROCK PAPER SCISORS - its best of three-  whats your choice? ')

        time.sleep(0.8)
        print('ok the computer chose {}'.format(cpu_randy.upper()))

        if cpu_randy=='rock' and first=='scisors' or cpu_randy=='scisors' and first=='paper':
            counter = counter + 1
            print ('sorry you lose! because {} beats {}'.format(cpu_randy,first))
            earned=-1

        elif cpu_randy=='paper' and first=='rock':
            counter = counter + 1
            print ( 'sorry you lose! because {} beats {}'.format(cpu_randy,first))
            earned=-1

        elif cpu_randy==first:
            counter = counter + 1
            print('sorry its a tie- the computer also chose the same')
            earned = 0

        elif earned>2:
            print('CONGRATS YOUVE WON THE GAME!')

        else:
            counter = counter + 1
            print ('Cograts you win! because {} beats {}'.format(first,cpu_randy))
            earned = +1




