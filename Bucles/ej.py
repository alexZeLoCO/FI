#n = líneas del cuadrado
#c = caracter con el que se dibuja el cuadrado
#columnas del cuadrado = 2*n
def Subrutina (n,c):
    for i in range (1,n+1,1):
        if (i==1 or i==n):
            for j in range (1,2*n+1,1):
                print(c,end="")
            print()
        else:
            print(c,end="")
            for j in range (1,2*n-1,1):
                print(" ",end="")
            print(c, end="")
            print()

n = int(input("Introduzca un valor natural: "))
c = input("Introduzca un caracter: ")
print (Subrutina(n,c))