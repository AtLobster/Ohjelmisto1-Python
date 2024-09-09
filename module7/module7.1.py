vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kk = int(input("Kerro kuukauden numero: "))


if kk in (12, 1, 2):
    vuodenaika = vuodenajat[3]
elif kk in (3, 4, 5):
    vuodenaika = vuodenajat[0]
elif kk in (6, 7, 8):
    vuodenaika = vuodenajat[1]
elif kk in (9, 10, 11):
    vuodenaika = vuodenajat[2]
else:
    print("Eihän tommosta kuukautta edes ole :D")

print(f'{kk}. kuukausi on {vuodenaika}')


"""vuodenaika = {"3":"kevättä",
              "4":"kevättä",
              "5":"kevättä",
              "6":"kesää",
              "7":"kesää",
              "8":"kesää",
              "9":"syksyä",
              "10":"syksyä",
              "11":"syksyä",
              "12":"talvea",
              "1":"talvea",
              "2":"talvea",}

kk = input("Kerro kuukauden numero: ")
if kk in vuodenaika:
    print(f'{kk}. kuukausi on {vuodenaika[kk]}')
"""



