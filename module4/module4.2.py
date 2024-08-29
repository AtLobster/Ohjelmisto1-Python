tuuma = float(input("Anna tuumat: "))
sentti = tuuma * 2.54

while tuuma >= 0:
    print(f'{sentti: .2f}cm')
    tuuma = float(input("Anna tuumat: "))
    sentti = tuuma * 2.54
