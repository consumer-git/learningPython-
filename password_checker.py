#build a login application

#ask for password in a specific format
#one cap, one special character and one number. minimum 6 letters

#generate a password and save it to text file

#retrive text file in login


def Validatepwd(p):
    letter_flag = False
    number_flag = False
    upper_case=False
    minimum=False
    for i in p:
        if i.isalpha():
            letter_flag = True
        if i.isdigit():
            number_flag = True
        if i.isupper():
            upper_case= True
        if len(p)>6:
            minimum=True


    return letter_flag, number_flag, upper_case, minimum

print(Validatepwd('Password123'))
