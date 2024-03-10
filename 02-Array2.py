import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tabla = pd.DataFrame(
    np.random.randint(0, 100, size=(4, 3)), 
    columns=["Pepe", "María", "Gaby"]
)

print(tabla)

tabla.plot()

plt.show()
