def  es_posible_ganar_con_n_piedras(n):
    lista = [False]*(n)
    for i in range(n):
        if i ==0 :
            pass
        elif i>0 and i<6:
            if lista[i-2]==False or lista[i-1]==False:
                lista[i]=True
        else:       #i>=6
            if lista[i-6]==False or lista[i-2]==False or lista[i-1]==False:
                lista[i]=True
    return lista[n-1]

print(es_posible_ganar_con_n_piedras(10**6))