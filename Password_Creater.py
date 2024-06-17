///Updated

import random

Values = "ASDFGHJKLZXCVQWERTYBNMUIOPasdfrewqtghjklpoiuymnbvcxz"
vari = "~!@#$%^&*()_+`1234567890-=[{;:',</?"

passwd = {}

for i in range (0,5) :
    passwd = { "".join(random.sample(Values+vari, 10)):i}
    print( i+1, ':', list(passwd.keys()))
