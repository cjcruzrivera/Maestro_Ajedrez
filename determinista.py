numeroIteraciones = 0

def Reinas(solucion,etapa,n,iteraciones):
    global numeroIteraciones
    numeroIteraciones += 1
    if etapa>=n:                             # si la etapa es mayor que n, entonces devolvemos falso
        return False
    exito = False                            # inicializamos exito a False
    
    while True:
            if (solucion[etapa] < n):                       # si el valor de la columna para la fila es mayor o igual que n, entonces no seguimos incrementando, con esto evitamos indices fuera del array.
                solucion[etapa] = solucion[etapa] + 1       # incrementamos el valor de columna para la reina i-esima de la fila i-esima.

            if (Valido(solucion,etapa)):                    # si la reina i-esima de la fila i-esima de la columna j en la etapa k no entra en conflicto con otra reina, proseguimos.

                if etapa != n-1:                            # si aun no hemos acabado todas las etapas, procedemos a la siguiente etapa.
                    exito = Reinas(solucion, etapa+1,n,iteraciones+1)
                    if exito==False:                        # si del valor devuelto de Reinas tenemos falso, ponemos a 0 el valor de la etapa + 1 para asi descartar los nodos fracaso.
                        solucion[etapa+1] = 0

                else:
                    print("Solucion DETERMINISTA: ")    
                    print solucion
                    print("Cantidad de iteraciones DETERMINISTA: "+str(numeroIteraciones))                    
                    exito = True
                    
            if (solucion[etapa]==n or exito==True):         # si el valor de la columna j de la etapa k es igual a n o exito es igual a True, salimos del bucle y devolvemos exito.
                break
    return exito


def Valido(solucion,etapa):
    # Comprueba si el vector solucion construido hasta la etapa es 
    # prometedor, es decir, si la reina se puede situar en la columna de la etapa

    for i in range(etapa):
        if(solucion[i] == solucion[etapa]) or (ValAbs(solucion[i],solucion[etapa])==ValAbs(i,etapa)):
            return False

    return True

def ValAbs(x,y):
    if x>y:
        return x - y
    else:
        return y - x    

def maestroDeterminista(cantidadReinas, numeroIter):

    solucion = []
    for i in range(cantidadReinas):
        solucion.append(0)
    etapa = 0
    
    Reinas(solucion, etapa, cantidadReinas, numeroIteraciones)
    
    return numeroIteraciones
