import random

heitotLkm = int(input("Montako kertaa noppaa heitetään: "))

summa = 0

for i in range(heitotLkm):
    h1 = random.randint(1,6)
    summa += h1
    i -= 1

print(f'Heittojen summa on {summa}.')