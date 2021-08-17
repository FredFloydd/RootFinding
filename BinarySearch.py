import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2 * x - 3 * np.sin(x) + 5


def binary_search(low_point, high_point, error, func):
    iterations = 0
    is_done = False
    while not is_done:
        iterations += 1
        mid_point = (low_point + high_point) / 2
        low_value, mid_value, high_value = func(low_point), func(mid_point), func(high_point)
        if low_value * mid_value < 0:
            if high_point - low_point < 2 * error:
                estimate = (low_point + mid_point) / 2
                print(f'Root estimate: {estimate}   Iterations: {iterations}')
                return estimate, iterations
            else:
                high_point = mid_point
        elif mid_value * high_value < 0:
            if high_point - low_point < 2 * error:
                estimate = (mid_point + high_point) / 2
                print(f'Root estimate: {estimate}   Iterations: {iterations}')
                return estimate, iterations
            else:
                low_point = mid_point
        else:
            return mid_point, iterations


truncationError = 0.5 * 10 ** -5
exactRoot = -2.88323687
offset = 1 * 10 ** -9
minPower = -18
maxPower = 10
numPoints = 10000

testWidths = np.logspace(minPower, maxPower, num=numPoints, base=2)
lowPoints = exactRoot - testWidths / 2 + offset
highPoints = exactRoot + testWidths / 2 + offset
rootEstimates = np.empty(testWidths.size)
iterationsTaken = np.empty(testWidths.size)

for i in range(testWidths.size):
    rootEstimates[i], iterationsTaken[i] = binary_search(lowPoints[i], highPoints[i], truncationError, f)

fig, ax = plt.subplots()

ax.plot(np.log2(testWidths), iterationsTaken, label='Iterations')
ax.set_xlabel('Log(Width of starting interval)')
ax.set_ylabel('Iterations taken')
ax.set_title('Dependence of iterations on initial interval width')
ax.legend()

plt.savefig('Plots/BinarySearch.png', dpi=300)
plt.show()
