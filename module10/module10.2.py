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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_lkm):
        self.hissit = []
        for i in range(hissi_lkm):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))


    def aja_hissia(self, hissin_nro, kohde):
        if 0 <= hissin_nro < len(self.hissit):
            self.hissit[hissin_nro].siirry_kerrokseen(kohde)

        else:
            print("Virhe")
            sys.exit()




talo = Talo(0, 10, 4)

talo.aja_hissia(3, 8) #Saatavilla olevat hissit ovat 0 -> hissi_lkm -1


#h = Hissi(0, 10)
#h.siirry_kerrokseen(4)


