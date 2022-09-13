import random as rnd
import matplotlib.pyplot as plt
import time
import math

def resta_matrices(a,b):
    resta = []
    for i in range(len(a)):
        resta.append([0]*len(a[i]))
        for j in range(len(a[0])):
            resta[i][j] = a[i][j] - b[i][j]
    return resta

def suma_matrices(a,b):
    suma = []
    for i in range(len(a)):
        suma.append([0]*len(a[i]))
        for j in range(len(a[0])):
            suma[i][j] = a[i][j] + b[i][j]
    return suma

def producto_escuela(a,b):
    producto = []
    for i in range(len(a)):
        producto.append([0]*len(a[i]))
        for j in range(len(a[0])):
            for k in range(len(a)):
                producto[i][j] += a[i][k]*b[k][j]
    return producto

def mult_strassen(a,b):
    n = len(a)

    #Caso base:
    if n <= 50:
        return producto_escuela(a,b)
    
    impar = False
    if n%2 != 0:
        impar = True
        ceros = [0]*(n+1)
        #anadimos un 0 a cada fila
        for i in range(n):
            a[i] += [0]
            b[i] += [0]
            
        #anadimos una fila de 0's
        a.append(ceros)
        b.append(ceros)
        n += 1
    
    #Separar en bloques
    a11 = [[a[i][j] for j in range (n//2)] for i in range(n//2)]
    a12 = [[a[i][j] for j in range (n//2,n)] for i in range(n//2)]
    a21 = [[a[i][j] for j in range (n//2)] for i in range(n//2,n)]
    a22 = [[a[i][j] for j in range (n//2,n)] for i in range(n//2,n)]
    
    b11 = [[b[i][j] for j in range (n//2)] for i in range(n//2)]
    b12 = [[b[i][j] for j in range (n//2,n)] for i in range(n//2)]
    b21 = [[b[i][j] for j in range (n//2)] for i in range(n//2,n)]
    b22 = [[b[i][j] for j in range (n//2,n)] for i in range(n//2,n)]
    
    #Algoritmo
    s1 = suma_matrices(a11,a22)
    s2 = suma_matrices(b11,b22)
    s3 = suma_matrices(a21,a22)
    s4 = suma_matrices(a11,a12)
    s5 = suma_matrices(b11,b12)
    s6 = suma_matrices(b21,b22)
    
    r1 = resta_matrices(b12,b22)
    r2 = resta_matrices(b21,b11)
    r3 = resta_matrices(a21,a11)
    r4 = resta_matrices(a12,a22)

    m1 = mult_strassen( s1,  s2)
    m2 = mult_strassen( s3,  b11)
    m3 = mult_strassen( a11, r1)
    m4 = mult_strassen( a22, r2)
    m5 = mult_strassen( s4,  b22)
    m6 = mult_strassen( r3,  s5)
    m7 = mult_strassen( r4,  s6)
                      
    c11 = resta_matrices(suma_matrices(suma_matrices(m1,m4),m7),m5)
    c12 = suma_matrices(m3,m5)
    c21 = suma_matrices(m2,m4)
    c22 = resta_matrices(suma_matrices(suma_matrices(m1,m3),m6),m2)                
    
    # CONSTRUIMOS LA NUEVA MATRIZ EN FNCION DE LOS CUATRO CUADRANTES    
    c = []
    for i in range(n//2):
        c.append([0]*n)
        for j in range(n//2):
            c[i][j] = c11[i][j]
        for j in range(n//2,n):
            c[i][j] = c12[i][j - n//2]
    for i in range(n//2,n):
        c.append([0]*n)
        for j in range(n//2):
            c[i][j] = c21[i - n//2][j]
        for j in range(n//2,n):
            c[i][j] = c22[i - n//2][j - n//2]
    
    #Si es impar borrar ultima fila y columna
    if impar:
        c.pop(n-1)
        for i in range(len(c)):
            c[i].pop(n-1)
    return c

mindigs = 2
maxdigs = 200
digstep = 1

numdigs = []
tiempos = []

n = mindigs
while n <= maxdigs:
    matriz_a = [] * n
    matriz_b = [] * n
    for i in range(n):
        matriz_a.append([0]*n)
        matriz_b.append([0]*n)
        for j in range(n):
            matriz_a[i][j] = rnd.randint(0,9)
            matriz_b[i][j] = rnd.randint(0,9)      
    ini = time.thread_time()
    matriz_c = mult_strassen(matriz_a,matriz_b)
    fin = time.thread_time()
    
    numdigs += [n]
    t = fin-ini
    tiempos += [t]
    n += digstep
    
plt.plot(numdigs, tiempos, "b-")
plt.xlabel('número de dígitos')
plt.ylabel('tiempo [seg]')
plt.savefig("grafica_strassen_tiempos.png")