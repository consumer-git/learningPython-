import random
import time


cpu_number=random.randint(1,10)

while True:

          time.sleep(1)

          welcome_note=("welcome to 'guess the number' \n I'm thinking of a number from 1 to 10. \n Can you guess?")
          print(welcome_note)
          time.sleep ( 1 )
          user_num=input('\n so tell me what number am I thinking of from 1 to 10? \n tell me! \n or press q to quit trying ')

          if user_num==cpu_number:
              print('congrats {} is the right answer'.format(cpu_number))

          elif user_num!=cpu_number:
              time.sleep ( 0.5 )
              print('OOPS! that is not the right answer! \n MY number was {} \n try again!'.format(cpu_number))


          elif user_num=='Q'.lower():
           break




