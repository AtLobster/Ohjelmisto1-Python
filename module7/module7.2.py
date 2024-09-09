nimet = set()

while True:
    nimi = input("Kerro nimi tai lopeta enterillä. ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Nimi on jo nimien joukossa. ")
    else:
        print("Uusi nimi lisätty joukkoon. ")
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)
