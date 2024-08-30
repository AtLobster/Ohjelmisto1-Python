mitta = float(input("Kerroppas minkä mittaisen kuhan nappasit:"))

if mitta<37:
    vajaa = 37 - mitta
    print(f'Päästäppä pikkukala kasvamaan {vajaa: .1f}cm')

else:
    kalajuttu = mitta * 2
    print(f'Itseppä olen napannut {kalajuttu: .0f}cm kuhan')
