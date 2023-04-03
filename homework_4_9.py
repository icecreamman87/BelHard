'''9. Создать матрицу, найти максимальное значение матрицы.'''

import random
matrix = [[random.randint(0,9) for j in range(4)] for i in range(3)]
print(matrix)
max_value = max(max(matrix, key=max))
print(max_value)