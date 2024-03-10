import numpy as np

arr = np.random.randint(0, 10, size=40)
print(f"{arr}\n")

print(f"{np.unique(arr)}\n") # Filtra los valores unicos de un array

print(f"{np.in1d([-1, 4, 8, 12], arr)}\n") # Busca si se encuentra los elementos de 1 array en otra array

array1 = np.random.uniform(-5,5, size=[3,2])

print(f"{array1}\n")

array2 = np.where(array1<0, 0, array1) # reemplaza los elementos de un array que cumplen con la condicion, en este caso los menores a 0.
print(f"{array2}\n")

array2 = np.where(array2>0, 2, array2)
print(f"{array2}\n")

