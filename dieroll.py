#simulate a die flip / best of three

import random

class Dieroll:

    def __init__(self,name,color):
        self.name=name
        self.color=color
        print('this is a {} die roll on a {} let the game begin'.format(self.color,self.name))

    def Roll(self,side):
        self.side=random.randint(1,6)

        print('and the roll is for {}'.format (self.side))

    def Addtolist(self,side):
        finallog=[]
        self.side=side
        for num in self.side:
            finallog.append(self.side)
            print('the final tally is {}'.format(finallog))



monday=Dieroll('monday','red')
monday.Roll('')    #hmmm, why did I have to place a '' in the argument?
monday.Addtolist('')  #cant get this function to work





