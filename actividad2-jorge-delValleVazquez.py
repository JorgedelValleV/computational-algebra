n=100                       #   indica el numero de cajas
pasos=0                     #   solucion del problema, indica los turnos que suceden hasta 
cajas= [1]*(n)              #   La lista que guarda la informacion de las bolas que hay en cada caja
vacias=0                    #   Se repite el estado inicial cuando vuelvan a estar todas las cajas con una que equivale a ninguna vacia, cuando eso suceda
end=False                   #  end tomara  el valor cierta y habremos acabado
indice=0
while not end:
    cantidad=cajas[indice]  # guardamos la cantidad de bolas a trasladar a las cajas consecutivas previo a poner que quedan 0 bolas en esa caja
    if cantidad!=0:         # el paso solo procede si hay alguna bola que mover en cuyo caso estamos realizando un paso y dejando una caja vacia
        cajas[indice]=0
        vacias+=1
        pasos+=1
        for i in range(cantidad):   #colocamos las bolas y dejamos el indice en aquella donde hemos depositado la bola en ultimo lugar
            indice=(indice+1)%n
            cajas[indice]+=1
            if cajas[indice]==1:
                vacias-=1
        if vacias==0:           # Si ya no quedan cajas vacias hemos llegado al estado buscado
            end = True
print(pasos)