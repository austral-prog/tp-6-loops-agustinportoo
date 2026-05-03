# Replace the "ANSWER HERE" for your answer

def index_of(target, lst):
    """
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """
    if target not in lst:
        return -1
    else:
        index=0
        for i in lst:
            index=lst.index(target)
        return index

def index_of_by_index(target, lst, start):
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """

    for indice,valor in enumerate(lst[start:]):
        if valor==target:
            return indice + start
    else:
        return -1

def index_of_empty(lst):
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """
    for indice,valor in enumerate(lst):
        if valor=="":
            return indice
    else:
        return -1
