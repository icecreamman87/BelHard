# Homework_2 (Lists)
# Task_1
import random
from typing import Set

list = [random.randint(-50, 50) for elem in range(20)]
print(list)
print(len(list), sum(list), sum(list) / len(list))

# Task_2
list = [random.randint(-50, 50) for elem in range(10)]
list.sort(reverse=True)
print(list)

# Task_3
list = [random.randint(-50, 50) for elem in range(10)]
print(list)
list_2 = list.copy()
list_2.remove(max(list))
print(list_2)
list_3 = list_2.copy()
list_3.insert(0, max(list))
print(list_3)

# Task_4
list = [random.randint(-50, 50) for elem in range(10)]
print(list)
list_pos = [elem for elem in list if elem > 0]
print(list_pos)
list_pos.sort(reverse=True)
print(list_pos)
list_neg = [elem for elem in list if elem <= 0]
print(list_neg)
list_neg.insert(0, list_pos)
print(list_neg)

# Task_5
list = [random.randint(-50, 50) for elem in range(10)]
print(list)
del list[:list.index(min(list))]
print(list)

