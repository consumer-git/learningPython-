#write a program in oop for adding items in cart - checking it against inventory and computing the amount



import time

class Inventrymangmnt:

    def __init__(self):
        self.slots=[] #sets slots to zero - its still a blank list

    def additem(self,item):
        self.slots.append(item) #you can add items one at a time
        print('added. the cart now has {} items and contains {}'.format(len(self.slots),self.slots))

    def reduce(self,item):
        self.slots.remove(item)
        print('removed, the cart now has {} items and contains {} '.format(len(self.slots),self.slots))

    def adddiscount(self,card):
        if len(self.slots)>=5 and card=='visa':
            print('youre entitled to a 50% discount!')
        else:
            print('buy {} more item(s) to avail of a discount or use a VISA CARD!'.format(5-len(self.slots)))



bigbasket=Inventrymangmnt()
bigbasket.additem('tomato')
time.sleep(0.8)
bigbasket.additem('garlic')
time.sleep(0.8)
bigbasket.additem('potato')
time.sleep(0.8)
bigbasket.additem('kari patta')
time.sleep(0.8)
bigbasket.additem('onion')
time.sleep(0.8)
bigbasket.additem('orange juice')
bigbasket.reduce('tomato')
bigbasket.reduce('potato')
bigbasket.reduce('onion')

bigbasket.adddiscount(card='visa')













# class Inventoryhandl:
#
#     def __init__(self):
#         self.slots=[]
#
#     def Addtoinv(self,item):
#         self.slots.append(item)
#         print('we have {} items in basket'.format(len(self.slots)))
#         print('basket includes {} '.format(self.slots))
#
#     def Delitem(self,item):
#         self.slots.__delitem__(item)
#         left=len(item)
#         print('we now have {} items in inventory'.format(left))
#
#
#
#
# bb=Inventoryhandl()
#
# bb.Addtoinv(item='tomato')
# bb.Addtoinv(item='potato')
#
#
#
