import random

def heitto(heittoMax):
    h = random.randint(1,heittoMax)
    return h

heittoMax = int(input("Nopan maksimi luku: "))

abc = 0

while abc != heittoMax:
    abc = heitto(heittoMax)
    print(abc)
