luvut = []
luku = input("Kerro kiva luku. ")
luvut.append(int(luku))

while luku != "":
    luku = input("Anna seuraava luku tai lopeta ohjelma tyhjällä merkinnällä: ")
    if luku != "":
        luvut.append(int(luku))
print("Suurin antamistasi luvuista on: ", int(max(luvut)))
print("Pienin antamistasi luvuista on: ", int(min(luvut)))
