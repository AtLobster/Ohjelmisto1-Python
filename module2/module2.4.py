kl1_str, kl2_str, kl3_str = input("Anna kolme lukua: ").split()

kl1 = float(kl1_str)
kl2 = float(kl2_str)
kl3 = float(kl3_str)

sum = kl1 + kl2 + kl3
avg = (kl1 + kl2 + kl3) / 3
cdot = kl1 * kl2 * kl3

print(f'Numeroiden summa on {sum}\nNumeroiden tulo on {cdot}\nNumeroiden keski-arvo on {avg}' )

