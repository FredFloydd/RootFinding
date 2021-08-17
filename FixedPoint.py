import numpy as np
import matplotlib.pyplot as plt


def fixed_point(func, initial_value, tolerance, max_n, k_=0):
    n = 0
    is_done = False
    values = np.array([initial_value])
    while not is_done:
        n += 1
        values = np.append(values, func(values[n - 1], k_))
        if np.abs(values[n] - values[n - 1]) < tolerance or n == max_n:
            is_done = True
    print(f'N = {len(values) - 1}   Root estimate = {values[-1]}')
    return values


def question_3_function(x, k_):
    return (3 * np.sin(x) + k_ * x - 5) / (2 + k_)


def question_4_function(x, k_):
    return (- x ** 3 + 8.5 * x ** 2 + 8) / 20


x_0 = 6
epsilon = 10 ** -5
n_max = 1000
k = 10

exactRoot = 4

values_by_step = fixed_point(question_4_function, x_0, epsilon, n_max, k)

x_min = -1
x_max = 5
num_points = 1000

x_values = np.linspace(x_min, x_max, num_points)
function_values = question_4_function(x_values, k)

fig, ax = plt.subplots()

ax.plot(x_values, function_values, label='y = f(x)')
ax.plot(x_values, x_values, label='y = x')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'Plot of y = f(x) and y = x from x = {x_min} to x = {x_max}')
ax.legend()

plt.savefig('Plots/FixedPoint/DoubleRootPlot.png', dpi=300)

error_plot_x_values = np.arange(1, values_by_step.size)
error_ratios = np.empty(len(values_by_step) - 1)
theoretical_ratios = np.empty(len(values_by_step) - 1)
for i in range(len(values_by_step) - 1):
    error_ratios[i] = np.abs((exactRoot - values_by_step[i]) / (exactRoot - values_by_step[i-1]))
    theoretical_ratios[i] = error_plot_x_values[i-1]/error_plot_x_values[i]

fig, ax = plt.subplots()

ax.plot(error_plot_x_values[1:], error_ratios[1:], label='Ratio of errors')
ax.plot(error_plot_x_values[1:], theoretical_ratios[1:], label='Theoretical ratio')
ax.set_xlabel('N')
ax.set_ylabel('Ratio')
ax.set_title('Plot of ratios of successive errors')
ax.legend()

plt.savefig('Plots/FixedPoint/FixedPointRatiosPlot.png', dpi=300)
print()
print(f'C = {error_ratios[-1]}')
