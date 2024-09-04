import math

def hintasuhde(diacm, hinta):

    radmetri = float((diacm / 2)) / 100
    ala = math.pi * radmetri ** 2
    suhde = float(hinta)/ala

    return suhde

def abc():
    halkaisija1 = float(input("Kerro ensimmäisen pizzan halkaisija senteissä: "))
    hinta1 = float(input("Kerro ensimmäisen pizzan hinta euroissa: "))

    halkaisija2 = float(input("Kerro toisen pizzan halkaisija senteissä: "))
    hinta2 = float(input("Kerro toisen pizzan hinta euroissa: "))

    suhde1 = hintasuhde(hinta1, halkaisija1)
    suhde2 = hintasuhde(hinta2, halkaisija2)

    if suhde1 > suhde2:
        print("Eka pizza")
    elif suhde2 < suhde1:
        print("Toka pizza")
    else:
        print("Molemmat")

    return

abc()



"""
hinta = input("Paljonko pizza maksoi euroina: ")
r2 = input("Kerro pizzan halkaisija: ")
suhde = hintasuhde(hinta, r2)

print(f'Ensimmäisen pizzan hinta on {suhde} euroa per neliömetri. ')
"""
"""
hinta2 = input("Paljonko pizza maksoi euroina:  ")
r22 = input("Kerro pizzan halkaisija: ")
suhde2 = hintasuhde(hinta, r2)

print(f'Toisen pizzan hinta on {suhde} euroa per neliömetri. ')

if suhde2 > suhde:
    print(f'Toisen pizzan hinta-määrä suhde on parempi.')
if suhde2 < suhde:
    print(f'Ensimmäkisen pizzan hinta-määrä suhde on parempi.')
"""