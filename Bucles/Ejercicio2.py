n = int(input("Introduzca un número natural: "))        #SOLICITA VALOR

while n<=0:     #MIENTRAS SEA NEGATIVO
    print ("Valor inválido")        #AVISO
    n=int(input("Introduzca un número natural: "))      #SOLICITA VALOR

for i in range (1,n+1,1):       #PARA N VECES
    for j in range (1,n+1,1):       #PARA N VECES
        print ("*",end="")      #OUTPUT    -   PARA LA MISMA FILA
    print()     #CAMBIO DE FILA
