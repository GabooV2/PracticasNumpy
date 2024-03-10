import numpy as np

array1 = np.arange(1, 6)
array2 = np.array([-3, 7, 3, 13, 0])

# OPERACIONES MATEMATICAS SIMPLES
# Suma
suma = np.add(array1, array2)
print(f"La suma de los arrays {array1} y {array2} es: {suma}\n")
# Resta
resta = np.subtract(array2, array1)
print(f"La resta de los arrays {array2} y {array1} es: {resta}\n")
# Raiz Cuadrada
raiz = np.sqrt(array1)
print(f"La raíz cuadrada del array {array1} es: {raiz}\n")
# La potencia (numero elevado a otro numero)
potencia = np.power(array1, 2)
print(f"La potancia del array {array1} elevado por 2 es: {potencia}\n")
# Devuelve el signo de los elementos de un array (si es 1, el numero es positivo y si es -1, el elemento es negativo y 0 es 0)
signo = np.sign(array2)
print(f"Los signos del array {array2} es: {signo}\n")

# FUNCIONES TRIGONOMETRICAS
# Seno
seno = np.sin(array1)
print(f"El seno del array {array1} es: {seno}\n")
# Coseno
coseno = np.cos(array1)
print(f"El coseno del array {array1} es: {coseno}\n")
# Tangente
tangente = np.tan(array1)
print(f"La tangente del array {array1} es: {tangente}\n")
# Grados en radianes
g2r = np.deg2rad(array1)
print(f"Los radianes del array {array1} es: {g2r}\n")
# Radianes en grados
r2g = np.rad2deg(array1)
print(f"Los grados del array {array1} es: {r2g}\n")

# OPERACIONES COMPARATIVAS

# Numero maximo por posicion entre 2 arrays.
print(f"El maximo entre los arrays {array1} y {array2} es: {np.maximum(array1, array2)}\n")
# Numero minimo por posicion entre 2 arrays.
print(f"El minimo entre los arrays {array1} y {array2} es: {np.minimum(array1, array2)}\n")
# condición "Igual Que" por posicion entre 2 arrays.
print(f"Condicion IGUAL QUE entre los arrays {array1} y {array2}: {np.equal(array1, array2)}\n")
# condición "Mayor Que" por posicion entre 2 arrays.
print(f"Condicion IGUAL QUE entre los arrays {array1} y {array2}: {np.greater(array1, array2)}\n")