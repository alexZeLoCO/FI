def primo (n):
    """

    :param n: Número a evaluar
    :return: Boolean si es o no primo
    """
    i=2
    while i<n/2 and n%i!=0:
        i+=1
    return n%i!=0

def primeros_n_primos(lista):
    """

    :param lista: A hallar los primos
    :return: Lista de primos
    """
    primos=[]
    for i in lista:
        if primo(i):
            primos.append(i)
    return primos

n=int(input("Introduzca un número n : "))
lista = range (1,n+1)
print (primeros_n_primos(lista))