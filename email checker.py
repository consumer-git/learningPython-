

#sources from emailtxtfile

fhandle=open('emails','r')
name=[]
domain=[]
for line in fhandle:
    singlemail=line.split(';')

    for email in singlemail:
        n,d =email.split('@')
        name.append(n)
        domain.append(d)

        print(name)















