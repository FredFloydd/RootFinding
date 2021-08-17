import numpy as np
import matplotlib.pyplot as plt

minPoint = -10
maxPoint = 10
numberOfPoints = 10000
inputPoints = np.linspace(minPoint, maxPoint, numberOfPoints)
functionValues = 2 * inputPoints - 3 * np.sin(inputPoints) + 5

fig, ax = plt.subplots()

ax.plot(inputPoints, functionValues, label='F(x)')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_xlabel('x')
ax.set_ylabel('F(x)')
ax.set_title(f'Plot of F(x) from x = {minPoint} to x = {maxPoint}')
ax.legend()

plt.savefig('Plots/Question1.png', dpi=300)
