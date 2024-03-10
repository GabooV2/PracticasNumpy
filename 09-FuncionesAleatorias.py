import numpy as np

# NUMEROS ALEATORIOS
print(f"numero decimal random entre 0 y 1 es => {np.random.rand()}\n")
print(f"array decimal 1D random entre 0 y 1 es => {np.random.rand(4)}\n")
print(f"array decimal 2D random entre 0 y 1 es => {np.random.rand(4,2)}\n")
print(f"array decimal 3D random entre 0 y N es => {np.random.uniform(10, size=[2,2,2])}\n")
print(f"array decimal 4D random entre N y M es => {np.random.uniform(-2,2, size=[2,2,2,2])}\n")
print(f"numero entero random entre 0 y N es => {np.random.randint(5)}\n")
print(f"array entero 1D random entre 0 y N es => \n{np.random.randint(10, size=[3])}\n")
print(f"array entero 2D random entre 0 y N es => \n{np.random.randint(10, size=[3,3])}\n")
print(f"array entero 3D random entre -N y M es => \n{np.random.randint(-5,5, size=[4,4,4])}\n")
print(f"array uniforme con curva gaussiana => \n{np.random.normal(size=20)}\n")

# PERMUTACIONES
arr = np.arange(10)
print(f"El array es =>  \n {arr}\n")

np.random.shuffle(arr)
print(f"Desordenando el array =>  \n {arr}\n")

n = 15
print(f"La permutacion de {n} elemento(s) es =>  \n {np.random.permutation(n)}\n")



