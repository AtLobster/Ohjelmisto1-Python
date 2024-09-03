import random

heitotLkm = int(input("Montako kertaa noppaa heitetään: "))

for i in range(heitotLkm):
    h1 = random.randint(1,6)
    print(f'{h1}')
    i -= 1
