
def gallonz(gallons):
    litres = gallons * 3.785
    return litres

gallons = 0

while gallons >= 0:
    gallons = float(input("Kerro polttoaineen määrä galloneissa: "))
    if gallons < 0:
        break

    litres = gallonz(gallons)
    print(litres)