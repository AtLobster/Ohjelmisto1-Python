def listsum(num):
    numlist = []
    num = 0

    while num != "":
        num = input("Kerro numero tai lopeta tyhjällä merkinnällä: ")
        if num != "":
            numlist.append(int(num))
    summa = sum(numlist)

    return summa

listings = []

listings = listsum(listings)
print(listings)
