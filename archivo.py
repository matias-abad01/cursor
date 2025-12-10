arreglo = [1, 2, 3, 4, 5]

def suma(arreglo):
    """
    Calcula la suma de todos los elementos de un arreglo.
    
    Args:
        arreglo: Lista de números a sumar.
    
    Returns:
        La suma total de todos los elementos del arreglo.
    """
    suma = 0
    for i in arreglo:
        suma += i
    return suma
total = suma(arreglo)

print("La suma de los elementos del arreglo es: ", total)

   
   


