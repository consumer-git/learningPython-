#create random password generator

import string
import random

l=string.ascii_lowercase
u=string.ascii_uppercase
d=string.digits
p=string.punctuation
# l1=l.split()
# u1=u.split()
# d1=d.split()
# p1=p.split()

count=16
quota=int(0.25*(count))

# seeder=l1+u1+d1+p1
finalchosenpassword=[]
choice=0
while choice<4:
    prt1=(random.choices(l))
    prt2= ( random.choices ( u) )
    prt3= ( random.choices ( d ) )
    prt4= ( random.choices ( p ) )
    choice+=1
    finalchosenpassword.append(prt1)
    finalchosenpassword.append ( prt2 )
    finalchosenpassword.append ( prt3 )
    finalchosenpassword.append ( prt4 )
    re=finalchosenpassword
    # print(re)


    implode=[''.join(x) for x in re]
    j=''.join(implode)
print('YOUR RANDOMLY GENERATED PASSOWRD IS: {}'.format(j) )





























