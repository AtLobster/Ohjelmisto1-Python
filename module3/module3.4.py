vuosil = float(input("Kerro vuosiluku:"))

kV = "Vuosi on karkausvuosi."
notkV = "Vuosi ei ole karkausvuosi."

if (vuosil % 4 == 0):
    if (vuosil % 100 == 0) and not (vuosil % 400 == 0):
        print(f"{notkV}")
    else:
        print(f"{kV}")
else:
    print(f"{notkV}")
