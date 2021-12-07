#UO281827 - EXAMEN LABORATORIO PYTHON 2, FUNDAMENTOS DE INFORMÁTICA. RODRÍGUEZ LÓPEZ, ALEJANDRO.
#EJERCICIO 2:

def contar_mayores (lista,n):
    """
    Subrutina contar_mayores(): Cuenta los elementos de la lista que sean estrictamente mayores que n.

    :param lista: Lista inicial.
    :param n: Parámetro con el que comparar.
    :return: Contador del número de elementos estrictamente mayores que n.
    """
    contador=0                 #OUTPUT DEBE SER EL Nº DE ELEMENTOS ==> CONTADOR
    for elemento in lista:         #PARA CADA ELEMENTO DE LA LISTA
        if elemento>n:         #SI ES MAYOR QUE EL PARÁMETRO
            contador=contador+1     #ACTUALIZAR CONTADOR

    return contador         #DEVOLVER CONTADOR

#COMPROBACIÓN
                          #LISTA
print(contar_mayores([2,3,2,1,5,7,10],3))          #OUTPUT (EXPECTED: 3)
                                     #N
print(contar_mayores([2,3,2,1,5,7,10],-4))         #OUTPUT (EXPECTED: 7)
print(contar_mayores([2,3,2,1,5,7,10],10))         #OUTPUT (EXPECTED: 0)
print(contar_mayores([2,3,2,1,5,7,10],1))          #OUTPUT (EXPECTED: 6)
