import matplotlib.pyplot as plt
import random

#funcion que calcula el simbolo_jacobi para este problema, no considera valores negativos de a( se puede solucionar pues a= -a*-1 calcular(-a/N) y multiplicar por -1 si N=3(mod 4))
def simbolo_jacobi(a, N):
    if (a == 0):
        return 0# (0/N) = 0
    jac = 1
    if (a == 1): #(1/N) = 1
        return jac
    while (a!=0):# lo mismo que while(a)

        #primero se reducen las potencias de 2
        while (a % 2 == 0):
            a = a // 2
            #(2/N) = -1 si N = 3 o 5(mod 4)
            if (N % 8 == 3 or N % 8 == 5):
                jac = -jac 
        
        a, N = N, a 
        #(a/N)(N/a)= -1 si a = 3 (mod 4) y N = 3 (mod 4)
        if (a % 4 == 3 and N % 4 == 3):
            jac = -jac
        
        #(a/N)=(a mod N / N)
        a = a % N 

    if (N == 1):
        return jac
    return 0


def solovay_strassen(p, k):
    if p== 2  :#2 es primo
        return True
    
    # si p es par entonces no es primo : si es par el ultimo bit es 0, por lo que al hacer not sera 1 y luego al hacer and con 1 se obtiene true
    if not p & 1: # not p & 1  = True sii p es par, mas eficiente que p%2==0
        return False

    # Asegurado que p>=3 primo
    for i in range(k):
        a = random.randint(1, p - 1)
        s = simbolo_jacobi(a, p)
        # Si s=(a/p) es 0 sabemos que gcd(a,p) de distinto de 1 luego p es compuesto		
        if s== 0:
            return False
        y = pow(a, (p - 1) // 2, p) # a^(p-1)/2 (mod p)
        # Si y es distinto de (a/p) (mod p) entonces [a] no pertenece a Tp y por tanto p es compuesto
        if (y != s % p):
            return False

    # p es primo con probabilidad de error menor que 1/2^k
    return True

def generar_primo(n,k=20):
    cnt=0
    p=0
    p_es_primo=False
    # probamos hasta encontrar un primo
    while(not p_es_primo):
        #generamos un numero de n cifras
        p=random.randint(1,(10**n)-1)
        #comprobamos si es primo
        p_es_primo= solovay_strassen(p,k)
        cnt+=1
    
    return (p,cnt)


def generar_histograma():
    n=300
    k=20
    x=100
    l=[]
    for i in range(x):
        l.append(generar_primo(n,k)[1])
    # dividimos el rango de valores obtenidos en 12 intervalos
    intervalos = range(min(l), max(l) + 2,(max(l)-min(l))//12)
    plt.hist(l,bins=intervalos,color="yellow",ec="blue",rwidth=0.85)
    plt.title("histograma actividad 7")
    plt.xlabel("cnt")
    plt.ylabel("frecuencia")
    plt.show()


generar_histograma()