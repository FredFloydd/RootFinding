import numpy as np
import matplotlib.pyplot as plt


def fixed_point(func, initial_value, tolerance, max_n):
    n = 0
    is_done = False
    values = np.array([initial_value])
    while not is_done:
        n += 1
        value, derivative = func(values[n - 1])
        values = np.append(values, values[n - 1] - value / derivative)
        if np.abs(values[n] - values[n - 1]) < tolerance or n == max_n:
            is_done = True
    print(f'N = {len(values) - 1}   Root estimate = {values[-1]}')
    return values


def equation_4_function(x):
    return 2 * x - 3 * np.sin(x) + 5, 2 - 3 * np.cos(x)


def equation_5a_function(x):
    return x ** 3 - 8.5 * x ** 2 + 20 * x - 8, 3 * x ** 2 - 17 * x + 20


x_0 = 2
epsilon = 10 ** -5
n_max = 100

exactRoot = 4
values_by_step = fixed_point(equation_5a_function, x_0, epsilon, n_max)

x_min = -50
x_max = 50
num_points = 100000
num_iterations_to_draw = 7

x_values = np.linspace(x_min, x_max, num_points)
function_values = x_values - equation_5a_function(x_values)[0] / equation_5a_function(x_values)[1]

fig, ax = plt.subplots()

ax.plot(x_values, function_values, label='y = f(x)')
ax.plot(x_values, x_values, label='y = x')

x_value_3 = x_0
y_value_3 = x_value_3 - equation_5a_function(x_value_3)[0] / equation_5a_function(x_value_3)[1]

min_x = x_0
min_y = y_value_3
max_x = x_0
max_y = y_value_3

for i in range(num_iterations_to_draw):
    x_value_1 = x_value_3
    y_value_1 = y_value_3

    x_value_2 = y_value_1
    y_value_2 = x_value_2
    x_value_3 = x_value_2
    y_value_3 = x_value_3 - equation_5a_function(x_value_3)[0] / equation_5a_function(x_value_3)[1]

    x_values_iteration = np.array([x_value_1, x_value_2, x_value_3])
    y_values_iteration = np.array([y_value_1, y_value_2, y_value_3])
    ax.plot(x_values_iteration, y_values_iteration, color='r')

    if x_value_2 < min_x:
        min_x = x_value_2
    elif x_value_2 > max_x:
        max_x = x_value_2

    if y_value_2 < min_y:
        min_y = y_value_2
    elif y_value_2 > max_y:
        max_y = y_value_2

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.xlim(np.floor(min_x) - 1, np.ceil(max_x) + 1)
plt.ylim(min_y - 1, max_y + 1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'Plot of y = f(x) and y = x from x = {np.floor(min_x) - 1} to x = {np.ceil(max_x) + 1}')
ax.legend()

plt.savefig('Plots/NewtonRaphson/Convergence.png', dpi=300)

error_plot_x_values = np.arange(1, values_by_step.size)
error_ratios = np.empty(len(values_by_step) - 1)
for i in range(len(values_by_step) - 1):
    error_ratios[i] = np.abs((exactRoot - values_by_step[i]) / (exactRoot - values_by_step[i - 1]))

fig, ax = plt.subplots()

ax.plot(error_plot_x_values[1:], error_ratios[1:], label='Ratio of errors')
ax.set_xlabel('N')
ax.set_ylabel('x_{N} / x_{N-1}^{2}')
ax.set_title('Plot of ratios for a single root')
ax.legend()

plt.savefig('Plots/NewtonRaphson/SingleRootRatiosPlot.png', dpi=300)
print()
print(f'C = {error_ratios[-1]}')
