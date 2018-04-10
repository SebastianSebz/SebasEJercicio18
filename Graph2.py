import numpy as np
import matplotlib.pyplot as plt

Data = np.loadtxt('dataEc2.txt')

x = Data[:,0]
y = Data[:,1]
z = Data[:,2]

h = 0.1
N = 10/h

xo = np.linspace(0, 10, N)
yo = np.cos(xo)

plt.figure()

plt.scatter(x, y)
plt.plot(xo, yo)
plt.plot(y,z, color = 'r')

plt.savefig('grafica2.pdf')




