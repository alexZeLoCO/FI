def sumatorio (lista, n):
    """

    :param lista:  Lista en la que operar
    :param n: Valor al que elevar cada elemento
    :return: Sumatorio de cada valor de la lista elevado a n.
    """
    suma=0
    for i in lista:
        suma = suma + i**n
    return suma

lista = [1,1,1,1]
n=2
print (sumatorio(lista,2))