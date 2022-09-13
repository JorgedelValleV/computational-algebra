from math import gcd
#usamos la version maximo comun divisor de math, serviria tambien cualquiera vista en clase

def primo(n):
    # 0 y 1 no son primos
    if n < 2:
        return False
    # 2 es el unico primo par
    if n % 2 == 0:
        return n == 2
    # si n es impar vemos que no tiene divisores, y basta comprobar hasta la raiz de n
    d=3
    while d*d<=n:
        if n%d==0:
            return False
        d+=2
    return True

def carmichael(N):
    # los numeros de carmichael son compuestos impares, es decir no son pares ni primos
    if N < 2 or N % 2 == 0 or primo(N):
        return False
    # para los enteros impares menores que N.
    # Basta calcluar hasta N porque para a > N se tiene que si a y N son coprimos tambien lo son (a mod N) y N (dem = contrarreciproco)
    #  y como hacemos modulos N con a ^ (N-1) mod N y equivale verlo para a mod N,
    #  nos centramos solo en estos posibles valores  3,5,...N-2 o N-1 si N es impar o par respectivamente
    for a in range(3, N, 2):
        # si a y N son coprimos
        # si no se cumple para algun a entonces N no es primo por lo que podriamos habernos ahorrado la comprobacion de primo(N) de arriba
        if gcd(a, N) == 1:
            # si para algun a se tiene que (a^(N-1)) mod N no es uno entonces no es carmichael 
            if pow(a, N - 1, N) != 1:
                return False

    return True

def imprimir_diez_carmichael():
    i=0
    k=0
    while i < 10:
        if carmichael(k):
            print(k)
            i+=1
        k+=1

imprimir_diez_carmichael()