def lista (fichero):
    datos=[]
    f=open(fichero)         #154 NºLíneas = f
    for i in f:                 #for (int i=0;i<f;i++) {
        datos.append(int(i))        #añadir a lista sig valor (fichero)
            #Lista datos contiene todos los elementos de fichero en Int.
    f.close()
    return datos

fichero = input ("Nombre de fichero: ")         #String = "datos.txt"
print (sum(lista(fichero)))
                #"datos.txt"
            #Datos[...]
        #Suma de todo Datos[]