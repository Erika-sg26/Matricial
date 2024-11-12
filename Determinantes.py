def det_2x2(matriz):
    # Extraer los elementos de la matriz
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1] 
    
    # Calcular el determinante
    determinante=a*d-b*c
    return determinante

# Ejemplo de uso:
A= [[1, 0], [0, 1]]
B= [[1, 0], [1, 0]]
C= [[1, 1], [9, 3]]
det=det_2x2(C)
print("El determinante es:", det)



def cofactor_3x3(matriz, i, j):
    
    ##Calcula el cofactor de un elemento en la posición (i, j) de una matriz 3x3.
    
    # Crear la submatriz 2x2 removiendo la fila i y la columna j
    submatriz = [fila[:j] + fila[j+1:]
    for k, fila in enumerate(matriz) if k != i]
    
    # Calcular el determinante de la submatriz 2x2
    det_submatriz=det_2x2(submatriz)
    
    # Calcular el cofactor aplicando el signo alternante (-1)^(i+j)
    cofactor=((-1)**(i+j))*det_submatriz
    return cofactor

# Ejemplo de uso:
#matriz = [[1, 2, 3], [0, 4, 5], [1, 0, 6]]
#i=2
#j=1  # Para el elemento en la posición (1,1)
#resultado = cofactor_3x3(matriz, i, j)
#print("El cofactor es:", resultado)


def det_3x3(matriz):
    ##Calcula el determinante de una matriz 3x3 usando la expansión por cofactores.
  
    # Expansión por cofactores en la primera fila (i = 0)
    determinante = (
        matriz[0][0]*cofactor_3x3(matriz, 0, 0) +
        matriz[0][1]*cofactor_3x3(matriz, 0, 1) +
        matriz[0][2]*cofactor_3x3(matriz, 0, 2)
    )
    return determinante

# Ejemplo de uso:
matriz = [[1, 2, 3], [0, 4, 5], [1, 0, 6]]
resultado = det_3x3(matriz)
print("El determinante es:", resultado)
