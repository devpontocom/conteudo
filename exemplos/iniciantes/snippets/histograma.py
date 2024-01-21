import numpy as np
import matplotlib.pyplot as plt

dados = np.random.normal(0, 1, 1000)
plt.hist(dados, bins=30)
plt.title("Histograma")
plt.show()