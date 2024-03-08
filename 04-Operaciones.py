import numpy as np

array1 = np.array([1,2,3,4])
array2 = np.array([5,6,7,8])
array3 = np.array([9,0])

print(f"{array1 + array2}\n") # Para operar los arrays tienen que tener la misma cantidad de elementos sino dará error
print(f"{array1 - array2}\n")
print(f"{array1 - array1}\n")
print(f"{array1 * array2}\n")
print(f"{array1 * 10}\n")
print(f"{array1 * np.array(10)}\n")
print(f"{array1 / array2}\n")
print(f"{array1 / 2}\n")
print(f"{array1 / np.array(2)}\n")
print(f"{1 / array1}\n")
print(f"{array1 ** -1.}\n")
print(f"{array1 ** array2}\n")

array2d_1 = np.array([[1,2],[3,4]])
array2d_2 = np.array([[5,6],[7,8]])
print(f"{array2d_1 + array2d_2}\n")
print(f"{array2d_1 * 3}\n")
print(f"{array2d_1 * np.array([5,10])}\n") # Solo se puede operar matrices 2D si las columnas de los arrays son iguales Ej: 2x2 con 1x2




