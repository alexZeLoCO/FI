#INICIALIZA SUMA
suma = 0
#INICIALIZA CONTADOR
contador = 0

n=int (input("Introduzca el primer valor: "))       #SOLICITA PRIMER VALOR

while n>=0:     #MIENTRAS N SEA MAYOR QUE 0

    contador = contador + 1  # ACTUALIZAR CONTADOR
    suma = suma + n  # ACTUALIZAR SUMA

    n = float(input("Introduzca el siguiente valor: "))  # SOLICITA SIGUIENTE VALOR

#SI NO SE HA INTRODUCIDO UN VALOR VÁLIDO, DIVIDIRÍAMOS ENTRE 0. DAREMOS VALOR 1 EN SU LUGAR.
if suma == 0:       #SI SUMA TOTAL ES 0
    contador = 1    #CONTADOR 1
    suma = 1        #SUMA 1

print("La media de los números introducidos es:", suma/contador)  # OUTPUT
