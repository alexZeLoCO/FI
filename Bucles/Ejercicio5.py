
n = int(input("Introduzca un natural: "))       #SOLICITA VALOR
while (n <= 0):     #MIENTRAS SEA NEGATIVO
    print("Valor inválido.")        #AVISO
    n = int(input("Introduzca un natural: "))       #SOLICITA VALOR

for i in range (1,n+1):
    valor=i
    suma=0

    while cifra==0:
        cifra=valor%10
        suma = suma+cifra**3
        valor=valor//10

    if (i==suma):
        print (i,suma)

