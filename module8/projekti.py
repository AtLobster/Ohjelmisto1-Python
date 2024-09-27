import random
import databases
from geopy.distance import great_circle

#KESKEENNNENENENENE


def getrandomAp():

    sql = """
    SELECT airport.name aName, country.name cName, latitude_deg, longitude_deg 
    FROM airport 
    JOIN country ON airport.iso_country = country.iso_country 
    WHERE airport.type LIKE 'large_airport%' 
    ORDER BY rand() 
    LIMIT 1"""

    cursor = databases.conn.cursor(dictionary=True)
    cursor.execute(sql)

    randAirport = cursor.fetchall()
    if randAirport: #Ettei ole olematon tulos, poistanko?
        columnNames = randAirport[0].keys()

    aName = randAirport[0]['aName']
    cName = randAirport[0]['cName']
    startPoint = randAirport[0]['latitude_deg'], randAirport[0]['longitude_deg']

    #print(aName, cName, startPoint)

    return aName, cName, startPoint



def wrongCountry():

    sql = """
    SELECT DISTINCT country.name, latitude_deg, longitude_deg
    from country
    JOIN airport ON country.iso_country = airport.iso_country
    WHERE airport.type LIKE 'large_airport%' 
    ORDER BY rand()
    LIMIT 5
    """

    cursor = databases.conn.cursor(dictionary=True)
    cursor.execute(sql)
    fivewrongCountries = cursor.fetchall()

    if fivewrongCountries:
        columnNames = fivewrongCountries[0:5].keys()
        print(columnNames)

    for i, row in enumerate(fivewrongCountries, start=1):
        print(f"Row {i}: {row}")

    return

wrongCountry()

def distance(startPoint, destPoint):

    alku = (startPoint)
    loppu = (destPoint)
    dist = great_circle(alku, loppu).kilometers

    return dist

"""
aName, cName, startPoint = getrandomAp()
wNamesAndCoords = wrongCountry(cName)
wNames = [country[0] for country in wNamesAndCoords]

countryChoices = [cName] + wNames
random.shuffle(countryChoices)

startLat, startLon = startPoint
print(f'Starting point: {cName}, {aName}, ({startLat}, {startLon})\n')

for country in wNamesAndCoords:
    destName = country[0]
    destPoint = (country[1], country[2])
    distancefrom = distance(startPoint, destPoint)
    print(f'Maassa {destName} sijaitsevan lentokentän etäisyys lähtöpisteestä on {distancefrom: .0f}km. Päätepisteen koordinaatit ovat {destPoint}. ')

print(f"\n{countryChoices}")
"""


"""

Teeppä kommentit.
tehdä tapa että pelaaja voi valita noista vaihtoehdoista
muita juttuja en jake pohtia

seuraavaks pitää tehä logiikka et toi valitsee vääristä maista x määrän y etäisyyden päästä. 


jossai vaiheessa muuta randairport ja wrongcountries 1 funktioksi 
sen pitäisi valita yksi niistä olemaan aloitus paikka.
hmm

muuta for country looppi funktioksi joka tuottaa listan sekalaisessa 
järj.

"""

