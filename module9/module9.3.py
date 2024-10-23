
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

    def kulje(self, aika):
        self.kMatka += aika * self.nopeus
        return



auto = Auto("ABC-123", 10, 1)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Auton rekisteritunnus: {auto.rek:s} \nNopeus: {auto.nopeus:d}km/h \nKuljettu matka: {auto.kMatka}km.")


auto.kulje(1)
print(f"Kuljettu matka2 {auto.kMatka}km")
