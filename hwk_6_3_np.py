# Task_3 - Решить линейное тензорное уравнение
import numpy as np

A = np.array([[[0, 2], [3, 4]], [[5, 8], [7, 8]]])
B = np.array([[[2, 10], [11, 12]], [[13, 14], [15, 16]]])
C = np.tensordot(A, B, axes=((1, 0), (0, 1)))
print(C)
