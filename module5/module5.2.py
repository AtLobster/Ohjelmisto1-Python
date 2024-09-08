luvut = []
luku = input("Kerro luku tai lopeta tyhjällä merkinnällä: ")
luvut.append(luku)

while luku != "":
    luku = input("Seuraava luku tai lopeta tyhjällä merkinnällä: ")
    if luku != "":
        luvut.append(luku)

if luku == "":
    luvut.sort(reverse=True)

suurimmat = luvut[:5]
print(f'{suurimmat}')