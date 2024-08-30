bioGender = input("Mikä on biologinen sukupuolenne? ")
hemoG = float(input("Entä hemoglobiiniarvonne grammaa per litra "))

while bioGender == "Mies":
    if 134 <= hemoG <= 195:
        print("Hemoglobiiniarvo on normaali.")
        break
    elif hemoG < 134:
        print("Hemoglobiiniarvo on matala!!")
        break
    elif hemoG > 194:
        print("Hemoglobiiniarvo on korkea! :(")
        break

while bioGender == "Nainen":
    if 117 <= hemoG <= 175:
        print("Hemoglobiiniarvo on normaali.")
        break
    elif hemoG < 117:
        print("Hemoglobiiniarvo on matala!!")
        break
    elif hemoG > 175:
        print("Hemoglobiiniarvo on korkea! :(")
        break





