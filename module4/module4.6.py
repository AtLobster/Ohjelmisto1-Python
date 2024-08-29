import random

radius = 1.000000
rangeX = -1.000000, 1.000000
rangeY = -1.000000, 1.000000
i = 0
N = float(input("Kerro arvottavien pisteiden lukumäärä: "))

n = []
while i < N:
    x = random.uniform(rangeX[0], rangeX[1])
    y = random.uniform(rangeY[0], rangeY[1])
    if x**2 + y**2 < 1:
        n.append(+1)
    i += 1
nLkm = len(n)
piiArvio = 4*nLkm/N
print(f'{piiArvio: .4f}')