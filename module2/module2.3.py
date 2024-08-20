height_str = input("Kerro suorakulmion korkeus: ")
width_str = input("Kerro suorakulmion kanta: ")
height = float(height_str)
width = float(width_str)

ala = height*width
piiri = 2*height+2*width

print(f'Suorakulmion pinta-ala on {ala}\nSuorakulmion piiri on {piiri}')
