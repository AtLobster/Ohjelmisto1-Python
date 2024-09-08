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
