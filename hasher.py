#This seems worst but I was trying on matrix level descripter, sorry to disappoint you.

def hasher( i,n):
    kb='ACBEUVDGHJFIK'
    ka='LNRQPTYOSMRWZX'
    kg,ki='24680','13579'

    haash=[]

    if i in kb:
        haash+=[str(ord(i)+n*n) + '!']
    elif i in ka:
        haash+=[str(ord(i)+n**3) +'@']
    elif i in kg:
        haash+=[str(i/2+n+14) +'$']
    else:
        haash+=[str(i*n+11) + '%']

    return haash

def unhasher(l,n):
    k=[]
    if '!' in l:
        i=l.index('!')
        k+=chr(l[i]-(n*n)-1)
    elif '@' in l:
        i=l.index('@')
        k+=chr(l[i]-n**3-1)
    elif '$' in l:
        i=l.index('$')
        k+=chr(l[i]*2-n-14-1)
    else:
        i=l.index('%')
        k+=chr(i/2-12)
    print(k)

passwd=input("enter password in capslock with number:")
n=len(passwd)
hased=hasher(passwd,n)
print(hased)

unhasher(hashed,n)
        
