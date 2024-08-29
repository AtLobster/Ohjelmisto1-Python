import random

kone = random.randint(1, 10)
arvaus = int(input("Arvaa lukua 1-10: "))

while arvaus != kone:
    if arvaus < kone:
        print('Liian pieni arvaus')
        arvaus = int(input("Arvaa lukua 1-10: "))
    if arvaus > kone:
        print('Liian suuri arvaus')
        arvaus = int(input("Arvaa lukua 1-10: "))
if arvaus == kone:
        print("Oiken!! Onnittelut voitosta :)")
