import random

class Auto:
    def __init__(self, rek, huippuNopeus):
        self.rek = rek
        self.huippuNopeus = huippuNopeus
        self.nopeus = 0
        self.kMatka = 0

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

    def tulosta_tiedot(self):
        return f"{self.rek}, {self.huippuNopeus}km/h"

class Sahkoauto(Auto):
    def __init__(self, rek, huippuNopeus, akkukapasiteetti):
        super().__init__(rek, huippuNopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def tulosta_tiedot(self):
        return f"{super().tulosta_tiedot()}: {self.akkukapasiteetti} kWh"

class Polttomoottoriauto(Auto):
    def __init__(self, rek, huippuNopeus, tankkikoko):
        super().__init__(rek, huippuNopeus)
        self.tankkikoko = tankkikoko

    def tulosta_tiedot(self):
        return f"{super().tulosta_tiedot()}: {self.tankkikoko} l"


sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)


sahkoauto.kiihdyta(random.randint(0, sahkoauto.huippuNopeus))
polttomoottoriauto.kiihdyta(random.randint(0, polttomoottoriauto.huippuNopeus))


print("Autojen tiedot alussa:")
print(sahkoauto.tulosta_tiedot(), f"Nopeus: {sahkoauto.nopeus} km/h")
print(polttomoottoriauto.tulosta_tiedot(), f"Nopeus: {polttomoottoriauto.nopeus} km/h")


for i in range(3):
    sahkoauto.kulje(1)
    polttomoottoriauto.kulje(1)


print("\nAutojen kulkemat matkat 3 tunnin jälkeen:")
print(f"Sähköauto ({sahkoauto.rek}): {sahkoauto.kMatka:.1f} km")
print(f"Polttomoottoriauto ({polttomoottoriauto.rek}): {polttomoottoriauto.kMatka:.1f} km")