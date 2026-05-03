# Replace the "ANSWER HERE" for your answer

def collatz_steps(n):
    """
    Retorna la cantidad de pasos necesarios para llegar a 1
    siguiendo la conjetura de Collatz:
      - Si n es par: n = n // 2
      - Si n es impar: n = 3 * n + 1

    n debe ser >= 1. Si n es 1, retorna 0 (ya esta en 1).

    Ejemplo: collatz_steps(6) -> 8
      6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1  (8 pasos)
    """

    if n<=1:
        return 0
    contador = 0
    while n>1:
        if n%2==0:
            par=n // 2
            n=par
            contador+=1
        else:
            impar=3 * n + 1
            n=impar
            contador+=1

    return contador

def collatz_sequence(n):
    """
    Retorna la secuencia completa de Collatz como una lista,
    comenzando desde n y terminando en 1.

    n debe ser >= 1. Si n es 1, retorna [1].

    Ejemplo: collatz_sequence(6) -> [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    if n<=1:
        return [1]
    resultado=[n]
    while n>1:
        if n%2==0:
            par=n // 2
            n = par
            resultado.append(n)
        else:
            impar=3 * n + 1
            n = impar
            resultado.append(n)
    return resultado
