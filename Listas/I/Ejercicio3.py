def ceros (lista):
    """

    :param lista:
    :return: La misma lista cambiando los valores negativos por ceros.
    """
    contador = 0
    for i in range(len(lista)):
        if lista[i]<0:
            contador+=1
            lista[i]=0
    return contador



lista = [-1,2,-1,2]
print (ceros(lista))
print (lista)