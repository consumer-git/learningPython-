#dice rolling simulator - using OOP
#this one is better - you can adjust the sides to less than or more than 6 - ignoring real world physical limitations


class Die:


    def __init__(self,side,name):
        self.side=side
        self.name=name
        print("{} sided {} Die are reset".format(self.side,self.name))

    def rolldie(self,tries):
         import random
         import time
         self.tries=tries
         dieone=range(1,self.side)
         dietwo=range(1,self.side)
         d1output=random.choice(dieone)
         d2output=random.choice(dietwo)

         time.sleep ( 0.9 )

         print('after {} tries the first die shows {}' .format (self.tries,d1output*self.tries))

         time.sleep(0.9)

         print('after {} tries the second die shows {}' .format (self.tries,d2output*self.tries))

         time.sleep ( 1.3 )

         print('total is {}'.format(d1output+d2output))


g=Die(3,'green')

g.rolldie(tries=1)









