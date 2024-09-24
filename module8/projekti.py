
import databases

def randomAirport():
    sql = """
    SELECT airport.name, country.name 
    FROM airport 
    JOIN country ON airport.iso_country = country.iso_country 
    WHERE airport.type LIKE 'large_airport%' 
    ORDER BY rand() 
    LIMIT 1"""
    #Valitaan satunnainen lentokenttä ja maa, jossa lentokenttä sijaitsee
    cursor = databases.conn.cursor()
    cursor.execute(sql)
    randAirport = cursor.fetchall()

    #Halutaan ulos satunnaisen lentokentän nimi ja maa
    airportName = randAirport[0][0]
    countryName = randAirport[0][1]

    #print(airportName, countryName)
    return airportName, countryName

def wrongCountry(exceptionCountry):
    sql = """
    SELECT DISTINCT country.name
    from country
    JOIN airport ON country.iso_country = airport.iso_country
    WHERE airport.type LIKE 'large_airport%' AND country.name != '{exceotionCountry}'
    ORDER BY rand()
    LIMIT 5
    """

    cursor = databases.conn.cursor()
    cursor.execute(sql)
    wrongCountries = cursor.fetchall()


    return [country[0] for country in wrongCountries]

airportName, countryName = randomAirport()
muuMaaMustikka = wrongCountry(countryName)

countryChoices = []
countryChoices.append(countryName)
countryChoices.append(muuMaaMustikka)

print(countryChoices)

"""
Pitää järjestää countryChoices lista random järjestyksesen ettei oikea 
ole aina ekana.
Tehä kommentit.
tehdä tapa että pelaaja voi valita noista vaihtoehdoista
muita juttuja en jake pohtia brian :D

"""


#print(f"Valitun lentokentän nimi {airportName} ja sijainti {countryName}.")
#print(f"Väärät vaihtoehdot: {muuMaaMustikka}")