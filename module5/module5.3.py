prime = int(input("Syötä luku: "))

for i in range(2, prime):
    if prime % i == 0:
        print(f'{prime} ei ole alkuluku.')
        break

    if prime % i != 0:
        print(f'{prime} on alkuluku.')
        break
