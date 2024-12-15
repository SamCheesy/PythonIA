import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

lista = [1, 2, 3]
#con np.array, creamos el array.
arr = np.array(lista)
print(arr)

lista_2d = [(2, 3, 4),
            (5, 6, 7),
            (8, 9, 0)]
arr = np.array(lista_2d)
print(arr)

#arr.shape es para mostrar la forma del arreglo.
print(arr.shape)
#arr.ndim es para saber las dimensiones de nuestro arreglo.
print(arr.ndim)
#nos da el tipo de dato que se guarda.
print(arr.dtype)
#Nos da cuantos datos tiene almacenada.
print(arr.size)
#Crear un arreglo especificando el tipo de dato con dtype.
arr = np.array(lista_2d, dtype='int16')
print(arr.dtype)
#crear un arreglo de ceros, especificando la cantidad de filas (primer valor) y de columnas (segundo valor).
arr = np.zeros((3,2))
print(arr)
#crear un arrego de unos, de la misma manera que zeros.
arr = np.ones((3,3))
#crear un arreglo de una dimensión con los valores del 0 al 9.
arr = np.arange(10)
print(arr)
#crear un arreglo de dos dimensiones con la forma 2x5 y valores del 0 al 9.
arr = np.arange(10).reshape(2,5)
print(arr)
#crear un arreglo que tenga del 10 al 20, con un incremento de 2.
arr = np.arange(10, 21, 2)
print(arr)
#crear un array con 11 valores entre el 10 y el 20. Se puede colocar otra cantidad de valores.
arr = np.linspace(10, 20, 11)
print(arr)
#graficar las funciones seno y coseno.
pi = np.linspace(0,2*pi,100)
seno = np.sin(pi)
coseno = np.cos(pi)
plt.plot(pi, seno)
plt.plot(pi, coseno)
#plt.show()

