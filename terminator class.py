import time
import random

class Terminator:

    bullets=100




    def __init__(self,name):
        self.name=name

        print('I am {} - a terminator sent from the future and I am initialised'.format(self.name))



    def Killeffect(self,victim):
        if victim>1:
                print('{} target detected! tracking target'.format(victim))
                return True

        else:
                print('no target to track')
                return False



    def Nightvision(self,lightlev):
        if lightlev<10:
            print ('light level at {}! night vision activated!'.format(lightlev))

        else:
            False


    def reload(self,bullets):
        if self.bullets>1:
            ammo=bullets - self.bullets

            print('reloading weapon... remaining ammo now at {} rounds'.format(-ammo))


        else:
            print('{} out of ammo. need bullets!'.format(self.name))


    def ChooseWeap(self,env):
        self.env=env
        weapon = ['shotgun', 'machinegun', 'waltherppk']
        if self.env=='hostile':
            print ('{} detected deploying {}'.format(self.env,random.choice(weapon)))
        else:
            print('holstering weapon')


time.sleep(0.5)
t100=Terminator('prakash')
time.sleep(0.9)
t100.Killeffect(victim=2)
time.sleep(1)
t100.Nightvision(lightlev=2)
time.sleep(1.5)
t100.reload(bullets=60)
time.sleep(2)
t100.ChooseWeap(env='hostile')

