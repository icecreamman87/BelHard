# Task_1 '''Будет текстовый файл с числами которые нужно использовать для создания массива.'''
import numpy as np

with open('1_test.txt', 'r') as f:
    lines = f.read().split('\n')
    print(lines)
numbers = list(map(float, lines))
array = np.array(numbers)
print(array)
