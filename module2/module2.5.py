leiv_str, naula_str, luodit_str = input("Anna leiviskät, naulat ja luodit: ").split()
leiv = float(leiv_str)
naula = float(naula_str)
luodit = float(luodit_str)

lg = luodit * 13.3
ng = naula * 32 * 13.3
leivg = leiv * 20 * 32 * 13.3
kokoMassa = lg + ng + leivg
kilot = kokoMassa // 1000
grammat = kokoMassa - kilot * 1000

print(f'Massa nykymitoissa on {kilot: .0f}kg ja {grammat: .1f}g.')