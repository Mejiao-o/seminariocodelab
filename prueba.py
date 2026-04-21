with open("memoria.txt", "r") as memoria:
    cuentas = memoria.readlines()
    countBottle = cuentas[0]
    countCookie = cuentas[1]
print(countBottle)
print(countCookie)
