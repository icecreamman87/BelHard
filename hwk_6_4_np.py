# Task_4 - Решить задачу поиска наименьших квадратов для линейного матричного уравнения.

import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([7, 8, 9])
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

print(x)
