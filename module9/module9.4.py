import random



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

autot = []

for i in range(1, 11):
    rek = f"ABC-{i}"
    huippuNopeus = random.randint(100,200)
    auto = Auto(rek, 0)
    auto.huippuNopeus = huippuNopeus
    autot.append(auto)

race_finished = False

while not race_finished:
    for auto in autot:
        deltaNopeus = random.randint(-10,15)
        auto.kiihdyta(deltaNopeus)

        auto.kulje(1)

        if auto.kMatka >= 10000:
            race_finished = True
            break

for auto in autot:
    print(f"Auto: {auto.rek} Huippunopeus: {auto.huippuNopeus}km/h Loppunopeus:{auto.nopeus}km/h Kuljettu matka:{auto.kMatka}km")
