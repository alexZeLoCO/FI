def media (lista):
    """

    :param lista:
    :return: Media de la lista usando sum() y len()
    """
    return sum(lista)/len(lista)

def media_nolen (lista):
    """

    :param lista:
    :return: Media de la lista usando for, dos variables suma y contador.
    """
    suma=0
    contador=0
    for i in lista:
        contador=contador+1
        suma=suma+i
    return suma/contador

lista=[1,2,3,4,12,5,32]
print(media(lista))
print(media_nolen(lista))