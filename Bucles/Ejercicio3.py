m = int(input("Introduzca un natural: "))       #SOLICITA VALOR
while (m<=0):       #MIENTRAS SEA NEGATIVO
    print ("Valor inválido.")       #AVISO
    m = int (input ("Introduzca un natural: "))     #SOLICITA VALOR

n = int(input("Introduzca un natural: "))       #SOLICITA VALOR
while (n <= 0):     #MIENTRAS SEA NEGATIVO
    print("Valor inválido.")        #AVISO
    n = int(input("Introduzca un natural: "))       #SOLICITA VALOR

for i in range (1,m+1):     #PARA M VECES
    for j in range (1,n+1):     #PARA N VECES
        cadena = "A"+str(i)+str(j)      #CREA CADENA -OPCIONAL-
        print(cadena,sep="",end=" ")       #OUTPUT
    print()     #CAMBIO DE FILA
