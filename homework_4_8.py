'''8. Напишите программу, в которой решается уравнение вида
А(А - 1)* x=sin(A) , причем при значении A = 0 должно вычисляться решение x= -1.
'''
#Уточнить условие и решение

import math
from math import sin

A = input("Введите A:")
try:
    A = float(A)
except ValueError:
    print("Проверьте число")
if A == 0:
    print("x=-1")
elif A == 1:
    print("Деление на ноль")
else:
    x = math.sin(A) / A * (A - 1)
    print(x)

