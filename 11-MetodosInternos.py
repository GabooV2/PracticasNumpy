import numpy as np

arr = np.arange(1,7).reshape(2,3)


# METODOS ESTADISTICOS
# Sumatorio
print(f"La suma de todos los elementos del array es: {arr.sum()}")
# Promedio
print(f"El promedio de todos los elementos del array es: {arr.mean()}")
# Desv. Standard
print(f"La desviación Estandard es: {arr.std()}")
# Varianza
print(f"La varianza es: {arr.var()}")

# METODOS DE ORDENACIÓN

arr1 = np.random.randint(-5,5, size=[3,3])

# Ordenar horizontalmente
arr1.sort()
print(f"Array ordenado horizontalmente\n{arr1}\n")

# Ordenar verticalmente
arr1.sort(0)
print(f"Array ordenado verticalmente\n{arr1}")


