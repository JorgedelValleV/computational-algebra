cadena = ""                     # cadena donde concatenamos lasucesion de los numeros 
for i in range (10**6):         # naturales haciendo uso de un bucle for
    cadena += str(i)
result= 1                       # variable que acumula el resultado
a=1
while a <=(10**6):              # obtenemos por medio de un bucle while los terminos d1,d10,d100,d1000,d10000,d100000,d1000000
    result*=int(cadena[a])
    a*=10
print(result)                   # mostramos el resultado