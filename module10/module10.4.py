import random


class Auto: #Aika merkittävä tunneissa.
    def __init__(self, rek, nopeus):
        self.rek = rek
        self.nopeus = nopeus
        self.kMatka = 0
        self.huippuNopeus = 142

    def kiihdyta(self, deltaNopeus):
        uusi_nopeus = self.nopeus + deltaNopeus
        if uusi_nopeus > self.huippuNopeus:
            self.nopeus = self.huippuNopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus


    def kulje(self, aika):
        self.kMatka += aika * self.nopeus


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            deltaNopeus = random.randint(-10, 15)
            auto.kiihdyta(deltaNopeus)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Auto':<10} {'Nopeus':<10} {'Matka':<10}")
        for auto in self.autot:
            print(f"{auto.rek:<10} {auto.nopeus:<10} {auto.kMatka:<10}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kMatka >= self.pituus:
                return True
        return False



def luo_autot(maara):
    autot = []
    for i in range(1, maara + 1):
        rek = f"Auto{i}"
        huippuNopeus = random.randint(100, 200)
        auto = Auto(rek, 0)
        auto.huippuNopeus = huippuNopeus
        autot.append(auto)
    return autot

def main():
    kilpailu_nimi = "Suuri romuralli"
    kilpailu_pituus = 8000
    autojen_maara = 10

    autot = luo_autot(autojen_maara)

    kilpailu = Kilpailu(kilpailu_nimi, kilpailu_pituus, autot)

    tunnit = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            print(f"Tunnin {tunnit} tilanne: ")
            kilpailu.tulosta_tilanne()

    print("Kilpailu on päättynyt!")
    kilpailu.tulosta_tilanne()


main()