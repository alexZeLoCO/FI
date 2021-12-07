#UO281827 - EXAMEN LABORATORIO PYTHON 2, FUNDAMENTOS DE INFORMÁTICA. RODRÍGUEZ LÓPEZ, ALEJANDRO.
#EJERCICIO 3:

def lista_pares(n):
    """
    Subrutina lista_pares(n): Devuelve una lista de números pares desde el 2 hasta la n pasada como parámetro.

    :param n: Número final de la lista devuelta. Necesariamente entero positivo.
    :return: Lista formada por los elementos pares de [2,n]. Si fuese posible. -Para n<2 la lista es vacía-.
    """
    lista = []          #NUEVA LISTA VACÍA

    for i in range(2,n+1,2):        #DESDE EL 2 HASTA LA N (INCLUIDA) DE 2 EN 2.
        lista.append(i)         #ACTUALIZAR LISTA

    #SI N<2, NO SE OPERA ==> LISTA VACÍA.
    return lista        #DEVOLVER LISTA

#COMPROBACIÓN
                  #N
print(lista_pares(10))      #OUTPUT (EXPECTED: [2,4,6,8,10])
print(lista_pares(-10))     #OUTPUT (EXPECTED: [])
print(lista_pares(2))       #OUTPUT (EXPECTED: [2])
print(lista_pares(7))       #OUTPUT (EXPECTED: [2,4,6])

