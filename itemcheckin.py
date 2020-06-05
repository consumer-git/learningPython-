#present a list of groceries with prices from a text
#choose the item and add to cart
#compute total bill



import math
import time

d={85: 'apples', 105: 'mangoes', 33: 'pears', 180: 'charger'}
cartfinal=[]

while True:
    def additem(item):
        print('welcome to M-shop the menu for the day is {} in price & item'.format(d))
        time.sleep ( 1 )

        item=input('what item do you need? ')
        for key,value in d.items():
            if item ==value:
                time.sleep(0.5)
                print ('thats great {} is availible and is priced at {} '.format(value,key))
                time.sleep ( 0.5 )
                consent = input ( 'can I add {} to your cart? '.format ( value ) )
                if consent=='Y'.lower():
                    cartfinal.append(key)
                    time.sleep ( 0.5 )
                    print('your total is {}'.format(math.fsum(cartfinal)))
                    continue
                else:
                    time.sleep ( 0.5 )
                    print('ok thanks for clarifying')
                    break



    (additem(''))


