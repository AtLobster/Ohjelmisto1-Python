
class Auto: #Aika merkittävä tunneissa.
    def __init__(self, rek, nopeus, aika=0):
        self.rek = rek
        self.nopeus = nopeus
        self.kMatka = nopeus * aika

auto = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus: {auto.rek:s}, huippunopeus: {auto.nopeus:d}km/h ja kuljettu matka: {auto.kMatka:d}km")
