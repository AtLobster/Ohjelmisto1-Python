
class Auto: #Aika merkittävä tunneissa.
    def __init__(self, rek, nopeus, aika=0):
        self.rek = rek
        self.nopeus = nopeus
        self.kMatka = nopeus * aika
        self.huippuNopeus = 142

    def kiihdyta(self, deltaNopeus):

        if self.nopeus + deltaNopeus <= self.huippuNopeus:
            self.nopeus += deltaNopeus
            if self.nopeus + deltaNopeus < 0:
                self.nopeus = 0
            return



auto = Auto("ABC-123", 10, 1)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Auton rekisteritunnus: {auto.rek:s}, nopeus tällä hetkellä: {auto.nopeus:d}km/h.")

auto.kiihdyta(-200)
print(f"\nNopeus jarrutuksen jälkeen: {auto.nopeus:d}")

