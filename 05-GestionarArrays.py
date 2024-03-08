import numpy as np

arr = np.arange(0,50,5)

print(f"{arr}\n")
print(f"Elemento en la primera posicion es: {arr[0]}\n")
print(f"Elemento en la quinta posicion es: {arr[4]}\n")
print(f"Elemento en la ultima posicion es: {arr[-1]}\n")

arr[-1] = 99
print(f"Elemento en la ultima posicion ahora es: {arr[-1]}\n")

print(f"Esta es una copia del array {arr[:]}\n")
print(f"Estos son los primeros 3 elementos del array {arr[:3]}\n")
arr[1:-1] = 50
print(f"Se modificaron todos los elementos del array menos el primero y el ultimo {arr}\n")

# para copiar un array sin modificar el original
array = np.arange(0,30,3)
sub_arr = array[0:4].copy()
sub_arr[:] = 99
print(f"{array}\n")
print(f"{sub_arr}\n")


