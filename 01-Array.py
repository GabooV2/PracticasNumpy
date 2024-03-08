import numpy as np

array = np.array([1,2,3,4,5.4546])

print(array)
print(type(array)) # Nos indica el tipo de arreglo que tenemos
print(array.ndim) # Nos indica la cantidad de dimensiones que tiene el arreglo
print(array.shape) # Nos indica la forma que tiene el arreglo separado por comas, es decir, 
                    #es una tupla de 1 o mas elementos segun las dimensiones del arreglo. en este ejercicio seria (5,) 
                    #donde 5 es la cantidad de elemento que posee la dimension 1

array2 = np.array([[1,2,3],[4,5,6]])

print(array2)
print(array2.ndim)
print(array2.shape)
print(array.dtype) # Nos indica el tipo de dato que contiene el array (float64, int32, <U1, etc)

array3 = np.array([["H","O","L","A"]])
print(array3.dtype)


