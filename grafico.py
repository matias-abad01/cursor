#crear un grafico con numpy

import numpy as np
import matplotlib.pyplot as plt

datos = np.array([1, 2, 3, 4, 5])
plt.plot(datos)
plt.title("Grafico de linea")
plt.xlabel("Indices")
plt.ylabel("Valores")
plt.show()

