def listsum():
    numlist = []
    tasaluvut = []
    num = 1

    while num != "":
        num = input("Kerro numero tai lopeta tyhjällä merkinnällä: ")

        if num != "":
            numlist.append(int(num))
            if int(num) %2 == 0:
                tasaluvut.append(int(num))

    print(tasaluvut)
    print(numlist)

    return numlist, tasaluvut

listsum()