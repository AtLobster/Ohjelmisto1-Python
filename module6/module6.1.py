import random

def heitto():
    h = random.randint(1,6)
    return h

abc = 0

while abc != 6:
    abc = heitto()
    print(abc)
