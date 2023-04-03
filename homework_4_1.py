'''1.Напишите программу, в которой пользователь вводит целое число
а программа определяет, сколько в этом числе цифр 0, 1, 2 и так далее
до 9.'''

import collections
from collections import Counter
x = input("Введите число ")
fig = Counter(x)
print(sorted(dict.items(fig)))



