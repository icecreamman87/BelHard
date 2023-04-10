# Task_2 '''Будет СЛАУ которую нужно решить методом Гаусса/Крамера.'''
# Variant_1(Крамер):

import numpy as np

matrix_A = np.array([[2, 5, 4], [1, 3, 2], [2, 10, 9]])
matrix_B = np.array([30, 150, 110])
determ_A = np.linalg.det(matrix_A)
print(determ_A)
matrix_A_1 = np.array([[30, 5, 4], [150, 3, 2], [110, 10, 9]])
matrix_A_2 = np.array([[2, 30, 4], [1, 150, 2], [2, 110, 9]])
matrix_A_3 = np.array([[2, 5, 30], [1, 3, 150], [2, 10, 110]])
determ_A_1 = np.linalg.det(matrix_A_1)
print(determ_A_1)
determ_A_2 = np.linalg.det(matrix_A_2)
print(determ_A_2)
determ_A_3 = np.linalg.det(matrix_A_3)
print(determ_A_3)
x = round(determ_A_1 / determ_A, 0)
y = round(determ_A_2 / determ_A, 0)
z = round(determ_A_3 / determ_A, 0)
print(f"x={x},y={y},z={z}")

# Variant_2

import numpy as np

matrix_A = np.array([[2, 5, 4], [1, 3, 2], [2, 10, 9]])
matrix_B = np.array([30, 150, 110])
x = np.linalg.solve(matrix_A, matrix_B)
print(x)
