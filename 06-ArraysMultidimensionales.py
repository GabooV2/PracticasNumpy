import numpy as np

array = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print(f"{array}\n")
print(f"{array[0]}\n")
print(f"{array[0][0]}\n")
print(f"{array[-1][-1]}\n")

# Para editar tambien se puede acceder al elemento de la siguiente forma
# array[-1][0] = 50
# print(f"{array}\n")

# Para copiar un array con slicing
print(f"{array[:,:]}\n")  # Copia todo el array

print(f"{array[:2,:]}\n")  # Copia solo 2 filas del array
print(f"{array[:,:1]}\n")  # Copia solo 1 columna del array
print(f"{array[:2,:2]}\n")  # Copia solo un array 2x2

# Editar los elementos de un array
array[:, 1:2] = 99  # Edita los elemenetos de la columna 2 del array
print(f"{array}\n")

# Fancy Index (Por ahora solo se hace c)
array2d = np.zeros((5, 10))
# Modificacion masiva de los elementos dentro de un array
array2d[[0, 2, -1]] = 5

print(f"{array2d}\n")
# Consultamos los elementos de un array a voluntad
print(f"{array2d[[0,1,1,1,0]]}\n")

# Bucles
array3 = np.ones((3, 3))  # Recorremos el array por fila
for fila in array3:
    print(f"{fila}\n")

for i, fila in enumerate(array3):
    for j, columna in enumerate(fila):
        array3[i][j] = len(fila) * i + j

print(f"{array3}\n")

array3d = np.array( # Esto es un array en 3D y se puede hacer en mas dimensiones con tan solo cambiar los elementos por nuevas listas.
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ]
)

print(f"Array 3D => {array3d}\n")

array4d = np.ones([2,2,2,2])

print(f"Array 4D => {array4d}\n")


arr = np.arange(9).reshape(3,3) # Para generar un array 2D 3x3 de un rango de 9 elemento
print(f"{arr}\n")

arr3d = np.arange(27).reshape(3,3,3) # Para generar un array 3D 3x3 de un rango de 27 elemento
print(f"{arr3d}\n")
