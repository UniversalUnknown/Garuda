import random

Values= "ASDFGHJKLZXCVQWERTYBNMUIOPasdfrewqtghjklpoiuymnbvcxz"
vari="~!@#$%^&*()_+`1234567890-=[{;:',</?"

n=len(Values)
for i in range(0,4):
    print("".join(random.sample(Values+vari, 10)))


