n = int(input("Introduzca un natural: "))       #SOLICITA VALOR
while (n <= 0):     #MIENTRAS SEA NEGATIVO
    print("Valor inválido.")        #AVISO
    n = int(input("Introduzca un natural: "))       #SOLICITA VALOR

a = int(input("Introduzca un natural: "))       #SOLICITA VALOR
while (a<=0):       #MIENTRAS SEA NEGATIVO
    print ("Valor inválido.")       #AVISO
    a = int (input ("Introduzca un natural: "))     #SOLICITA VALOR
min = 1000000000000000000000000000000

for j in range (1,n+1):
    contador = 0        #CONTADOR
    for i in range (1,j+1):
        if (j%i==0):
            contador=contador+1
    if contador==a:
        print(j,"tiene",a,"divisores")
        if j<min:
            min=j

print("El menor valor es:",min)