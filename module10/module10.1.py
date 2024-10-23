import sys

class Hissi:

    kerros = 0

    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros


    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin_kerros or kohde > self.ylin_kerros:
            print("Kerrosvalinta ei mahdollinen.")
            sys.exit()


        while self.kerros < kohde and kohde < self.ylin_kerros:
            self.kerros_ylos()

        while self.kerros > kohde:
            self.kerros_alas()


        return

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}.")

        return

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1

            print(f"Hissi on kerroksessa {self.kerros}.")

        return

h = Hissi(0, 10)
h.siirry_kerrokseen(4)


