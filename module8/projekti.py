import random
import databases
from geopy.distance import great_circle

def randomAirport():
    sql = """
    SELECT airport.name, country.name, latitude_deg, longitude_deg 
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
    startPointLat = randAirport[0][2]
    startPointLon = randAirport[0][3]

    #print(airportName, countryName)
    return airportName, countryName, startPointLat, startPointLon

def wrongCountry(exceptionCountry):
    sql = """
    SELECT DISTINCT country.name
    from country
    JOIN airport ON country.iso_country = airport.iso_country
    WHERE airport.type LIKE 'large_airport%' AND country.name != '{exceptionCountry}'
    ORDER BY rand()
    LIMIT 5
    """

    cursor = databases.conn.cursor()
    cursor.execute(sql)
    wrongCountries = cursor.fetchall()


    return [country[0] for country in wrongCountries]


airportName, countryName, startPointLat, startPointLon = randomAirport()
muuMaaMustikka = wrongCountry(countryName)

countryChoices = [countryName] + muuMaaMustikka
random.shuffle(countryChoices)

print(countryName)
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