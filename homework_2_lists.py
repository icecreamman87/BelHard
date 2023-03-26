# Homework_2 (Lists)
# Task_1
import random

list_ = [random.randint(-50, 50) for elem in range(20)]
print(list_)
print(len(list_), sum(list_), sum(list_) / len(list_))

# Task_2
list_1 = [random.randint(-50, 50) for elem in range(10)]
list_1.sort(reverse=True)
print(list_1)

# Task_3
list_n = [random.randint(-50, 50) for elem in range(10)]
print(list_n)
list_2 = list_n.copy()
list_2.remove(max(list_n))
print(list_2)
list_3 = list_2.copy()
list_3.insert(0, max(list_n))
print(list_3)

# Task_4
list_4 = [random.randint(-50, 50) for elem in range(10)]
print(list_4)
list_pos = [elem for elem in list_4 if elem > 0]
print(list_pos)
list_pos.sort(reverse=True)
print(list_pos)
list_neg = [elem for elem in list_4 if elem <= 0]
print(list_neg)
list_neg.insert(0, list_pos)
print(list_neg)

# Task_5
list_5 = [random.randint(-50, 50) for elem in range(10)]
print(list_5)
del list_5[:list_5.index(min(list_5))]
print(list_5)

