import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='k1ssa',
    database='flight_game',
    collation = 'utf8mb4_unicode_ci',
)


def hae_lentokentan_tiedot():
    kursori = conn.cursor()
    icao = input("Anna lentoaseman ICAO-koodi: ")

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    if tulos:
        nimi, kunta = tulos
        print(f"\nLentoaseman tiedot:")
        print(f"Nimi: {nimi}")
        print(f"Kunta: {kunta}")
    else:
        print(f"ICAO-koodilla {icao} ei löytynyt lentokenttää.")


    kursori.close()
    conn.close()



hae_lentokentan_tiedot()