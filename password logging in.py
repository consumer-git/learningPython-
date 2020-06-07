#need to add a password checker to this & maybe wrap in a function?

while True:
    welcome=input('are you a returning player? ')
    if welcome=='N'.lower():



         username=input('please choose your username ')
         password=input('please choose your password ')
         combo=username+' '+password
         with open('db.txt', 'w') as f:
            f.write(combo)
            print('username and password logged')
            continue


    else:
        with open ( 'db.txt', 'r' ) as f:
            comboref=f.read()


        chkusername=input('whats your username? ')
        chkpasswd=input('whats your password? ')
        chkcombo=chkusername+' '+chkpasswd
        if chkcombo==comboref:
            print('welcome to the program!')
            break
        else:
            print('sorry thats wrong!')











