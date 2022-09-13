import random
import time


def multiplicacion_escuela(a, b):
    if len(a) != 2 or len(a[0]) != 2 or len(b) != 2 or len(b[0]) != 2:
        raise Exception('Matrices should be 2x2!')
    #print(a[0][0] * b[0][1] + a[0][1] * b[1][1])
    nueva = [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                  [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    return nueva


def suma_matrices(a, b):
    return [[a[fila][col] + b[fila][col] for col in range(len(a[fila]))] for fila in range(len(a))]


def resta_matrices(matrix_a, matrix_b):
    return [[matrix_a[fila][col] - matrix_b[fila][col] for col in range(len(matrix_a[fila]))] for fila in range(len(matrix_a))]


def separar_matriz(a):
    
    if len(a) % 2 != 0 or len(a[0]) % 2 != 0:
        raise Exception('Odd matrices are not supported!')

    tam = len(a)
    mitad = tam // 2
    a11 = [[a[i][j] for j in range(mitad)] for i in range(mitad)]
    a21 = [[a[i][j] for j in range(mitad)] for i in range(mitad, tam)]

    a12 = [[a[i][j] for j in range(mitad, tam)] for i in range(mitad)]
    a22 = [[a[i][j] for j in range(mitad, tam)] for i in range(mitad, tam)]

    return a11, a12, a21, a22


def get_dim(matrix):
    return len(matrix), len(matrix[0])


def strassen(a, b):
    if get_dim(a) != get_dim(b):
        raise Exception(f'Both matrices are not the same dimension! \nMatrix A:{b} \nMatrix B:{b}')
    if get_dim(a) == (2, 2):
        return multiplicacion_escuela(a, b)

    a11, a12, a21, a22 = separar_matriz(a)
    b11, b12, b21, b22 = separar_matriz(b)

    m3 = strassen(a11, resta_matrices(b12, b22))
    m5 = strassen(suma_matrices(a11, a12), b22)
    m2 = strassen(suma_matrices(a21, a22), b11)
    m4 = strassen(a22, resta_matrices(b21, b11))
    m1 = strassen(suma_matrices(a11, a22), suma_matrices(b11, b22))
    m7 = strassen(resta_matrices(a12, a22), suma_matrices(b21, b22))
    m6 = strassen(resta_matrices(a11, a21), suma_matrices(b11, b12))

    c11 = suma_matrices(resta_matrices(suma_matrices(m1, m4), m5), m7)
    c12 = suma_matrices(m3, m5)
    c21 = suma_matrices(m2, m4)
    c22 = suma_matrices(suma_matrices(resta_matrices(m1, m2), m3), m6)

    
    nueva = []
    for i in range(len(c12)):
        nueva.append(c11[i] + c12[i])
    for i in range(len(c22)):
        nueva.append(c21[i] + c22[i])
    return nueva



def init_matrices(f, c):
    M = []
    for i in range(f):
        M.append([])
        for j in range(c):
            M[i].append(random.randint(0,10))
    return M

def mostrarMat(M):
    print("\n")
    for fila in M:
        print(fila)
    print("\n")


def producto_matrices(a, b):
    n = len(a)
    m = len(b)
    p = len(a[0])
    q = len(b[0])
    if p != m:
        return None
    # Asignar espacio al producto. Es decir, rellenar con "espacios vacíos"
    producto = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        producto.append([])
        for j in range(q):
            producto[i].append(None)
    # Rellenar el producto
    for c in range(q):
        for i in range(n):
            suma = 0
            for j in range(p):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto

print("    Programa que multiplica 2 matrices    ")
orden = int(input("Generar orden: "))

A = init_matrices(orden,orden)
B = init_matrices(orden,orden)

mostrarMat(A)
mostrarMat(B)

print("Strassen")
inicio = time.time()
C = strassen(A,B)
fin = time.time()
mostrarMat(C)
tStrassen = fin -inicio

print("Tradicional")
inicio = time.time()
D= producto_matrices(A,B)
fin = time.time()
mostrarMat(D)
tTradicional = fin -inicio
print("Tiempo de strassen: " , tStrassen)
print("Tiempo de normal: " , tTradicional)