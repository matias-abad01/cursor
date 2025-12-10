import pandas as pd
import numpy as np
 

arreglo = [1, 2, 3, 4, 5]
df = pd.DataFrame(arreglo)
print(df)

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



   
   


