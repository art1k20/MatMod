import numpy as np
import math
def objective(x): #функція
    return (x[0] - 152 - 12)**2 + (x[1] - 156 + 12)**2
def s1_constraint(x): #s1
    return x[0]**2/156 + x[1]**2/(152 + 12) - 2.7 * (math.sqrt(12) + (152 * 156)**(1/12))
def s2_constraint(x): # s2
    return x[0]**2/156 + x[1]**2/(152 + 12) - 2.7 * (12**(1/2) + (152 * 156)**(1/12)) + 12**(1/2) * math.sin(x[0]) - (156 * 152)**(1/12) * math.cos(x[1])
def gradient(x): #градієнт функції f
    dfdx0 = 2 * (x[0] - 152 - 12)
    dfdx1 = 2 * (x[1] - 156 + 12)
    return np.array([dfdx0, dfdx1])
learning_rate = 0.01
max_iterations = 100
tolerance = 1e-6

x3 = np.array([0.0, 0.0])
for i in range(max_iterations):
    grad = gradient(x3)
    x3 += learning_rate * grad
    s2_value = s2_constraint(x3)
    k = i + 1
    print('Iteration ', k, ':\nx = ', x3[0], ', y = ', x3[1], '\nf(x,y) = ', objective(x3), '\ns2(x,y) = ', s2_value, sep = '')
    if abs(s2_value) < tolerance:
        break
max_x = x3[0]
max_y = x3[1]
max_value = objective(x3)
print('\nМаксимум f(x, y) на лінії s2:\nx_max = ', max_x, ', y_max = ', max_y,'\nМаксимальне значення f(x_max, y_max) = ', max_value, sep = '')