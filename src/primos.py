def ehPrimo(n):
    cont = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cont += 1

    if cont == 2:
        return True
    else:
        return False


def primosMenores(num):
    for i in range(num):
        if ehPrimo(i) == True:
            print(i)


num = int(input("Numero: "))
primosMenores(num)

