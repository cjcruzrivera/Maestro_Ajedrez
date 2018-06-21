import random

numeroIteraciones = 0

def solucionVegas(n):
    # Crea un vector con la ubicacion de n reinas en orden aleatorio
    reinas = random.sample(range(n), n)

    # Verificando diagonales en 45 grados
    for i in reversed(range(n)):
        columna45 = reinas[i]
        for j in reversed(range(i)):
            columna45 = columna45-1
            if (columna45 >= 0) & (columna45 <= n-1):
                if(columna45 == reinas[j]):
                    return False

    # Verificando diagonales en 135 grados
    for i in reversed(range(n)):
        columna135 = reinas[i]
        for j in reversed(range(i)):
            columna135 = columna135+1
            if (columna135 >= 0) & (columna135 <= n-1):
                if(columna135 == reinas[j]):
                    return False

    return reinas

def maestroVegas(cantidadReinas, exito, solucion, numeroIteraciones):
	
	while exito == False:
	    y = solucionVegas(cantidadReinas)
	    numeroIteraciones = numeroIteraciones + 1
	    solucion = y
	    exito = y

	print("Solucion VEGAS: ")
	print(solucion)
	print("Cantidad de iteraciones VEGAS: "+str(numeroIteraciones))

	return numeroIteraciones