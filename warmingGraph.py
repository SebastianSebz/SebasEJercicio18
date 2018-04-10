import numpy as np
import matplotlib.pyplot as plt

Data = np.loadtxt('dataEc.txt')

x = Data[:,0]
y = Data[:,1]

z = np.exp(x)

plt.figure()

plt.scatter(x, y)
plt.plot(x, z, color = 'c', lw = 5)

plt.savefig('grafica1.pdf')

