# Replace the "ANSWER HERE" for your answer

def find_min(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el menor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_min([3, 1, 7, 2]) -> 1
    Ejemplo: find_min([5, 5, 5]) -> 5
    Ejemplo: find_min([-3, -1, -7]) -> -7
    """
    minimo_actual = numbers[0]
    for i in numbers:
        if i < minimo_actual:
            minimo_actual = i
    return minimo_actual

def find_max(numbers):
    """
    Dada una lista de numeros (no vacia), retorna el mayor valor.
    Usar un bucle for para recorrer la lista.

    Ejemplo: find_max([3, 1, 7, 2]) -> 7
    Ejemplo: find_max([5, 5, 5]) -> 5
    Ejemplo: find_max([-3, -1, -7]) -> -1
    """
    maximo_actual=numbers[0]
    for i in numbers:
        if i>maximo_actual:
            maximo_actual=i
    return maximo_actual


def count_negatives(numbers):
    """
    Dada una lista de numeros, retorna la cantidad de numeros negativos.
    Si la lista esta vacia, retorna 0.

    Ejemplo: count_negatives([3, -1, -7, 2]) -> 2
    Ejemplo: count_negatives([1, 2, 3]) -> 0
    Ejemplo: count_negatives([-1, -2, -3]) -> 3
    """
    if len(numbers)==0:
        return 0
    contador=0
    for i in numbers:
        if i<0:
            contador+=1
    return contador
