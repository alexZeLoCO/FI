def contar (fichero):
    datos=[]
    f=open(fichero)         #154 NºLíneas = f = NºAlumnos
    contador=0
    for i in f:                 #for (int i=0;i<f;i++) {
        contador = contador + 1
            #Lista datos contiene todos los elementos de fichero en Int.
    f.close()
    return contador

def importar (fichero):
    datos = []
    f = open(fichero)  # 154 NºLíneas = f
    for i in f:  # for (int i=0;i<f;i++) {
        datos.append(i)  # añadir a lista sig valor (fichero)
        # Lista datos contiene todos los elementos de fichero en Int.
    f.close()
    return datos

def apellidos (linea,apellido,datos):
    return (apellido in datos[linea])

def cuenta_nombre (linea):
    pos = linea.index(',') + 2
    nombre = linea[-len(linea) + pos:]

    contador=0
    for i in range (len(nombre)):
        if (nombre[i]==" "):
            contador=contador+1

    return contador+1

fichero = input ("Nombre del fichero: ")
print (contar(fichero))      #EJ1

apellido=input("Introduzca apellido: ")
linea = int (input ("Introduzca línea: "))
print (apellidos(linea,apellido,  importar(fichero)  ))
                                #-----Churrera 1-----
        #----------------Churrera 2----------------
#---------------Churrera Industrial--------------------

suma=0
for i in range (0,len(importar(fichero)),1):                    #for (int i=0;i<importar(fichero).length;i++) {
    if(apellidos(i,"Fernandez",importar(fichero))):
        suma=suma+1

print (suma/len(importar(fichero))*100,"%",sep="")

linea = int(input("Introduzca la linea: "))
datos = importar(fichero)
apellidosYnombre=datos[linea]
print (cuenta_nombre(apellidosYnombre),"palabras.")

vector = [0,0,0,0,0]
for i in range (0,len(datos),1):
    apellidosYnombre = datos[i]
    vector[cuenta_nombre(apellidosYnombre)]=vector[cuenta_nombre(apellidosYnombre)]+1

for i in range (1,len(vector),1):
    print ("Personas con,",i,"palabras en el nombre:",vector[i])
