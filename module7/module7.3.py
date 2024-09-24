
lentokentta = {}
valinta = 0

while valinta != "":
    print("Valitse 1-3: ")
    print("1. Syötä uusi lentokenttä ")
    print("2. Hae olemassaoleva lentokenttä ")
    print("3. Exit")

    valinta = input("\nKerro valintasi: ")

    if valinta == "1":
        icao_code = input("Syötä ICAO-koodi: ")
        if icao_code in lentokentta:
            print("Tämä lentokenttä on jo tietokannassa. \n")
        else:
            nimi = input("Syötä lentokentän nimi: ")
            lentokentta[icao_code] = nimi
            print(f'{nimi} lisätty lentokenttien tietokantaan. \n')

    elif valinta == "2":
        icao_code = input("Kerro ICAO-koodi, jolla etsitään lentokenttää: ")
        if icao_code in lentokentta:
            print(f"\nICAO-koodia vastaava lentokenttä on: {lentokentta[icao_code]}. \n")
        else:
            print("\nKyseiseen ICAO-koodiin vastaavaa lentokenttää ei löydetty. \n")

    elif valinta == "3":
        break

    else:
        print("Valitse joko 1, 2 tai 3. ")

