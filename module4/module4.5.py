tunnus = "Atte"
salis = "ettA"

user = input("Käyttäjätunnus: ")
pw = input("Salasana: ")
yritykset = 0

if user == tunnus and pw == salis:
    print("Tervetuloa")

while user != tunnus or pw != salis and yritykset <= 4:
    print('Pääsy evätty.')
    user = input("Käyttäjätunnus: ")
    pw = input("Salasana: ")
    yritykset += 1
    if yritykset == 4:
        print('Tunkeilija havaittu')
        break
    if user == tunnus and pw == salis:
        print("Tervetuloa")