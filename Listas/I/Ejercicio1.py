def suma (lista):
    """

    :param lista:
    :return: Sumatorio de los elementos de la lista usando un for
    """
    suma=0
    for i in lista:
        suma = suma + i
    return suma

lista = [1, 1, 1, 1, 1]
print (suma(lista))
print (sum(lista))