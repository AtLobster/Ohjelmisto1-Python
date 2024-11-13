import json
import requests

city = input("Enter which citys' weather you'd like to see: ")
apikey = "01a80f826f649a6d231ac5ee3a997d4f"

coords = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid={apikey}"
kaupunki_info = requests.get(coords).json()


lat = kaupunki_info[0]["lat"]
lon = kaupunki_info[0]["lon"]
name = kaupunki_info[0]["name"]

weatherapi = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}&units=metric"
weather = requests.get(weatherapi).json()

print(f'City: {name}, {weather["main"]["temp"]} degrees celsius, feels like {weather["main"]["feels_like"]}. \n{weather["weather"][0]["main"]}, {weather["weather"][0]["description"]}, {weather["wind"]["speed"]} m/s')
