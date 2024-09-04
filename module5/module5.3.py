prime = int(input("Syötä kokonaisluku yli 2: "))

for i in range(2, prime):
    if prime % i == 0:
        print(f'{prime} ei ole alkuluku.')
        break

    if prime % i != 0:
        print(f'{prime} on alkuluku.')
        break


