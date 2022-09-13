import random as rnd
import math
def criba(n):
   l = [2] * (n+1) # 2 = aun no se si es primo o compuesto
   l[0] = l[1] = 0 # indico que 0 y 1 no son primos
   i = 2 # empiezo con el indice 2
   while i <= n:
      if l[i] == 2: # si no lo he tachado
         l[i] = 1 # lo marco como primo
         j = 2*i # busco los indices j=2i,3i,4i,...
         while j <= n: # hasta llegar a n y los marco
            l[j] = 0 # como compuestos
            j += i
      i += 1
   return l
   
def calculo_beta(B,N):
    primos=criba(B)
    beta =1
    for p in range(len(primos)):
        if(primos[p]):
            beta*= p**(math.ceil(math.log(N,p)))
    return beta
    
def pmenos1_pollard (N,B):
    a = rnd.randint(1,N-1)
    #primero vemos si a es divisor de N, por lo que devolvemos los factores a y N/a
    cociente,resto = divmod(N,a)
    if resto == 0:
        return (a,cociente)
    #Procedemos al calculo de beta y de a^beta - 1
    #Como beta es el producto de los p^ceil(log(N,p) con p primo menor igual que B 
    # podemos ir haciendo las sucesivas potencias de a por cada factor del producto,
    # en vez de hacer el calculo total de beta y entonces hacer la potencia
    primos = criba(B)
    for p in range(len(primos)):
        if primos[p]: #si i es primo, entonces primos[i]=1
            factor_beta = p**math.ceil(math.log(N,p))
            a = pow(a,factor_beta,N)
    y = math.gcd(a-1,N)
    if y != 0:
        print("gcd(a^beta - 1,N) = ", y," es un factor")
        return (y,N/y)
    # si no se da lo anterior repetimos el proceso con un nuevo calculo usando un nuevo valor para a
    return pollard(N)
    
B=100
N= 1542201487980564464479858919567403438179217763219681634914787749213
pollard=pmenos1_pollard(N,B)

print("Factores de ", N, " son: ", *pollard)