import numpy as np
import matplotlib.pyplot as plt

universe = np.zeros((6, 6))

beacon = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]

universe[1:5, 1:5] = beacon

plt.imshow(universe, cmap='binary')
plt.show()