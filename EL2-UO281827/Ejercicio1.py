#UO281827 - EXAMEN LABORATORIO PYTHON 2, FUNDAMENTOS DE INFORMÁTICA. RODRÍGUEZ LÓPEZ, ALEJANDRO.
#EJERCICIO 1:

#APARTADO A
def maximo(lista1,lista2):
    """
    Subrutina maximo(): Devuelve un máximo o una suma de mínimos en función de la longitud de los parámetros.

    :param lista1: Lista inicial 1
    :param lista2: Lista inicial 2
    :return: Mayor elemento de la lista más larga. La suma de sus menores si son iguales en longitud.
    """
        #OPTIMIZANDO
    len1=len(lista1)        #LONGITUD 1
    len2=len(lista2)        #LONGITUD 2
        #-----------

    if (len1<len2):       #SI LISTA 2 ES MAYOR
        return max(lista2)              #DEVOLVER MAXIMO DE LISTA 2
    elif (len1>len2):     #SI LISTA 1 ES MAYOR
        return max(lista1)              #DEVOLVER MAXIMO DE LISTA 1
    else:                 #SI NO -SON IGUALES-
        return min(lista1)+min(lista2)  #DEVOLVER SUMA DE MENORES

#APARTADO B
lista1=[2,3,4]           #LISTA 1
                  #LISTA 2
print(maximo(lista1,[8,9]))        #OUTPUT (EXPECTED: 4)

                 #NUEVA LISTA 2
print(maximo(lista1,[8,9,13]))        #OUTPUT (EXPECTED: 10)
