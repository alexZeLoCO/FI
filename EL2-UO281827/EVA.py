def sumar (fichero):
    """
    Subrutina sumar. Recibe un documento y transforma sus números -uno por fila- en una lista.
    :param fichero: Fichero con números enteros.
    :return: Suma los valores en posiciones pares, resta los demás.
    """
    datos = []          #LISTA DE ELEMENTOS
    f = open(fichero)  #ABRIR FICHERO
    for i in f:  #PARA CADA ELEMENTO DEL DOCUMENTO
        datos.append(int(i))  #AÑADIR ELEMENTOS A LISTA
    f.close()       #CERRAR EL ARCHIVO

    suma=0      #SUMATORIO
    for i in range (0,len(datos),1):  #PARA TANTOS ELEMENTOS COMO EN LA LISTA
        if i%2==0:      #SI INDICE ES PAR
            suma = suma + datos[i]      #SUMAR
        else:           #SI NO
            suma = suma - datos[i]      #RESTAR

    return suma         #RETURN

def suma_divisores(n):
    """
    Subrutina suma_divisores.
    :param n: Número entero.
    :return: Sumatorio de sus divisores -excepto él mismo-.
    """
    suma=1          #EL 1 ES SIEMPRE DIVISOR
    for i in range (2,n-1,1):           #PARA CADA ELEMENTO DESDE EL 2 HASTA EL ANTERIOR A N
        if i%n==0:          #SI ES DIVISOR
            suma=suma+i             #SUMATORIO
    return suma         #RETURN

def crea_archivo(n,string):
    """
    Subrutina crea_archivo. Crea un archivo con los números desde el 1 hasta la n diciendo si son o no iguales al
            sumatorio de sus divisores.
    :param n: Número entero.
    :param string: Cadena a leer.
    """
    f=open(string,'w')          #CREA ARCHIVO EN MODO ESCRIBIR          IMPORTANTE PARA CREAR ARCHIVO
    for i in range (1,n+1,1):           #PARA CADA NÚMERO DESDE EL 1 HASTA LA N
        boolean = str(i==suma_divisores(i))         #SI ES IGUAL A LA SUMA DE DIVISORES
        valor = str(i)          #NÚMERO

        f.write(valor+boolean+"\n")         #AÑADIR A LA LÍNEA              IMPORTANTE PARA CREAR ARCHIVO
    f.close()       #CERRAR ARCHVO                  IMPORTANTE PARA CREAR ARCHIVO

def ejercicio3 (n,texto1,texto2):
    """
    Subrutina ejercicio3. Crea un documento con los números de un documento que sean diferentes al parámetro.
    :param n: Número al que comparar.
    :param texto1: Documento con el que comparar.
    :param texto2: Nombre del documento a crear/escribir
    :return: Nuevo documento.
    """
    datos = []          #CREA VECTOR DE DATOS
    f = open(texto1)            #ABRE FICHERO
    for i in f:         #PARA CADA ELEMENTO
        datos.append(int(i))        #AÑADIR ELEMENTO

    f.close()           #CIERRA DOCUMENTO

    f = open(texto2, 'w')           #CREA DOCUMENTO
    for i in datos:         #PARA CADA ELEMENTO DE DATOS
        if i!=n:            #SI ES DIFERENTE A LA N
            txt = str(i)            #AÑADIR
            f.write(txt+"\n")       #AÑADIR
        else:           #SI NO
            f.write("\n")       #NO AÑADIR, SALTO DE LINEA
    f.close()           #CERRAR DOCUMENTO

def ejercicio4 (string,n):
    """
    Subrutina ejercicio4. Devuelve la suma de elementos menores a un parámetro de una lista.
    :param string: Lista de elementos.
    :param n: Número entero con el que comparar.
    :return: Sumatorio de números estrictamente menores que el parámetro.
    """
    suma=0      #INICIALIZAR SUMATORIO
    for i in string:            #PARA CADA ELEMENTO DE LA CADENA
        if len(i)<n:            #SI LA LONGITUD ES MENOR
            suma=suma+1         #ACTUALIZAR SUMATORIO
    return suma                 #RETORNAR SUMATORIO

print("Elija una de las opciones escribiendo el número que la indica: ")
print("1 Función sumar.")
print("2 Función crea_archivo.")
print("3 Función ejercicio3.")
print("4 Función ejercicio4.")
selección=int(input("Selección: "))
if selección==1:
    print("Se ha seleccionado la opción 1: Función sumar.")
    fichero = input("Introduzca nombre del fichero: ")
    print("Suma:", sumar(fichero))

elif selección==2:
    print("Se ha seleccionado la opción 2: Función crea_archivo.")
    n = int(input("Introduzca número: "))
    nom = input("Introduzca nombre: ")
    crea_archivo(n, nom)

elif selección==3:
    print("Se ha seleccionado la opción 3: Función ejercicio3.")
    n = int(input("Introduzca número: "))
    nom = input("Introduzca nombre archivo a leer: ")
    nom1 = input("Introduzca nombre archivo a escribir: ")
    ejercicio3(n, nom, nom1)

elif selección==4:
    print("Se ha seleccionado la opción 4: Función ejercicio4.")
    lista = ["uno", "dos", "tres", "cuatro"]
    print(ejercicio4(lista, 4))
