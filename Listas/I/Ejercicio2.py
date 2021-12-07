def mayor (lista):
    """

    :param lista:
    :return: El índice del mayor elemento de la lista.
    """
    mayor = lista[0]
    maximo_indice=None
    for i in range (len(lista)):
        if lista[i] > mayor:
            mayor=lista[i]
            maximo_indice=i
    return maximo_indice

lista = [1,3,2,5,8,0]
print (mayor(lista))