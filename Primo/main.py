n=int(input("Introduzca un número: "))      #SOLICITA VALOR
i=2     #INICIALIZA I

while not(n%i==0) and i<(n/2.0):     #MIENTRAS Y NO SEA DIVISOR Y SEA MENOR QUE LA MITAD DE N
    i=i+1       #AUMENTAR VALOR DE I

if i>(n/2.0):       #SI LA I ES MAYOR A LA MITAD DE N (NO SE ENCONTRÓ DIVISOR)
    print("No se ha encontado ningún divisor de",n,". El número es primo.")     #OUTPUT
else:       #SI NO (SE ENCONTRÓ UN DIVISOR)
    print("El número",i,"es divisor de",n,"por lo tanto, no es primo.")     #OUTPUT