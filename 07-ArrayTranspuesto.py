import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array Normal 2x3: \n {arr} \n")

print(f"Array Transpuesto 3x2: \n {arr.T} \n")

print(f"Array Transpuesto del Transpuesto: \n {arr.T.T} \n")

print(f"Array Transpuesto por medio de swapaxes: \n {arr.swapaxes(1,0)} \n")

arr3d = np.arange(8).reshape(2,2,2)
print(f"Array 3D: \n {arr3d} \n")
print(f"Array 3D Transpuesto: \n {arr3d.T} \n")
print(f"Array 3D Transpuesto con swapaxes por la profundidad: \n {arr3d.swapaxes(0,2)} \n")
print(f"Array 3D Transpuesto con swapaxes por el alto: \n {arr3d.swapaxes(0,1)} \n")
