def importar (fichero):
    """
    Subrutina importar. Importa los elementos de un fichero.

    :param fichero: Nombre del fichero.
    :return: Lista con los elementos del fichero.
    """
    datos = []  # LISTA DE ELEMENTOS
    f = open(fichero)  # ABRIR FICHERO  STR             -SE ABRE EL TELÓN-
    for i in f:  # PARA CADA ELEMENTO DEL DOCUMENTO
        datos.append(int(i))  # AÑADIR ELEMENTOS A LISTA    -ENTRAN LOS ACTORES-
    f.close()  # CERRAR EL ARCHIVO              -SE CIERRA EL TELÓN-
    return datos

print(sum(importar("datos.txt")))

def importarNombres(fichero):
    nombres=[]
    f=open(fichero)
    for i in f:
        nombres.append(i)
    f.close()
    return nombres

def contar (lista):
    contador=0
    for i in lista:
        contador=contador+1
    return contador

def coincide_apellido(cad,apellido):              #A IN B ==> EL ELEMENTO A ESTÁ EN B
    return apellido in cad

lista=(importarNombres("alumnos.txt"))
print(contar(lista))                                    #EXPCT OUT: 898

print(coincide_apellido(lista[0],"Rodriguez"))          #EXPCT OUT: TRUE
print(coincide_apellido(lista[5],"Rodriguez"))          #EXPCT OUT: FALSE

contador=0
for nombres in lista:
    if coincide_apellido(nombres,"Fernandez"):
        contador=contador+1
print("Hay un ",contador/contar(lista)*100,"% de personas con el apellido Fernández.",sep="")
