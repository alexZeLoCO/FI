def leer_lista():
    """

    :return: Lista formada por los valores introducidos.
    """
    lista=[]        #NUEVA LISTA
    n=int(input("Introduzca un entero: "))          #SOLICITA VALOR
    lista.append(n)         #ALMACENA PRIMER VALOR

    while (n<=50 and n>=-50):           #MIENTRAS LOS VALORE ESTÉN EN [-50,50]
        n=int(input("Introduzca un entero: "))          #SOLICITA VALOR
        lista.append(n)         #ANEXA VALOR

    return lista[:-1]           #CORTA EL ÚLTIMO -INVÁLIDO- Y DEVUELVE

def escala_lista(lista,n):
    """

    :param lista: Lista inicial.
    :param n: Número por el que multiplicar.
    :return: Vector formado por la nueva lista y el sumatorio de la lista multiplicada.
    """
    suma=0          #SUMATORIO
    for i in range(0,len(lista),1):         #PARA CADA ELEMENTO DE LA LISTA
        lista[i]=lista[i]*n     #ACTUALIZAR VALOR DE LA LISTA
        suma=suma+lista[i]       #SUMAR LOS VALORES MULTIPLICADOS

    return [lista, suma]    #OUTPUT, UN VECTOR FORMADO POR LA LISTA Y LA SUMA.

def compara_lista(lista1,lista2):
    """

    :param lista1: Lista primera
    :param lista2: Lista segunda
    :return: Boolean si son iguales
    """
    if (not bool (len(lista1)-len(lista2))):
        suma=0          #CREA UNA SUMA
        for i in range (0,len(lista1),1):           #PARA TANTOS ELEMENTOS DE LA LISTA
            suma=suma+abs(lista1[i]-lista2[i])       #LA SUMA ES LA DIFERENCIA ENTRE VALORES

            #LA ESTRATEGIA:
            #   CLARAMENTE, SI LA DIFERENCIA ENTRE TODOS LOS ELEMENTOS ES 0, ES PORQUE TODOS SON IGUALES. QUEDARÍA LA SUMA=0
            #   PODEMOS CONVERTIR SUMA EN BOOLEAN USANDO BOOL(SUMA), PERO DEVOLVERÍA FALSE SÓLO EN EL CASO EN QUE ÉSTA SEA 0,
            #   SI SUMA ES UN VALOR DIFERENTE -POSITIVO, NEGATIVO, ETC...- DEVOLVERÍA TRUE.
            #
            #   ÉSTO ES JUSTO LO OPUESTO A LO QUE QUEREMOS, POR LO QUE PODEMOS AÑADIR NOT AL PRINCIPIO DE LA ÓRDEN PARA QUE
            #   DEVUELVA TRUE CUANDO LA SUMA SEA 0 Y FALSE EN EL RESTO DE OCASIONES.

        return not bool (suma)      #OUTPUT
                          #0
                     #FALSE             SUPONIENDO QUE SON IGUALES
                  #TRUE
    else:
        return bool (0)

print("***** PRIMERA LISTA *****")      #OUTPUT
lista1=leer_lista()         #CREA LISTA 1
print("***** SEGUNDA LISTA *****")      #OUTPUT
lista2=leer_lista()         #CREA LISTA 2
print("***** TERCERA LISTA *****")      #OUTPUT
lista3=leer_lista()         #CREA LISTA 3

print("***** COMPARACIÓN DE LISTAS *****")      #OUTPUT
print(compara_lista(lista1,lista2))         #OUTPUT
print(compara_lista(lista2,lista3))         #OUTPUT

print("***** TERCERA LISTA x2 Y SU SUMA*****")          #OUTPUT
print("Lista inicial:",lista3)          #OUTPUT
nuevalista3=escala_lista(lista3,2)          #NUEVA LISTA IGUAL AL DOBLE
print("La nueva lista:",nuevalista3[0])         #OUTPUT PRIMER ELEMENTO (LISTA)
print("La suma es igual a:",nuevalista3[1])         #OUTPUT SEGUNDO ELEMENTO (SUMA)

