# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    resultado=[]
    for listas in matrix:
        for elementos in listas:
            resultado.append(elementos)
    return resultado

def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    resultado=[]
    for listas in matrix:
        suma_fila=0
        for numeros in listas:
            suma_fila+=numeros
        resultado.append(suma_fila)
    return resultado

def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    num_colms=len(matrix[0])
    resultado=[]
    for col in range(num_colms):
        suma_col = 0
        for listas in matrix:
            suma_col+= + listas[col]
        resultado.append(suma_col)
    return resultado
