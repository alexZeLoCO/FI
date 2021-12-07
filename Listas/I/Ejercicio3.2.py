def ceros (lista):
    """

    :param lista:
    :return: La misma lista quitando los valores negativos.
    """
    contador = 0
    i = 0

    while i < len(lista):
        if lista[i] < 0:
            contador += 1
            lista.pop(i)
        i = i + 1


    return contador


lista = [-1,2,-1,2]
print (ceros(lista))
print (lista)