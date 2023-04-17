#Task_1
'''Написать ф-цию, которая выводит ряд Фибоначии до заданной границы N.'''
# def fib(n):
#     a,b=0,1
#     while a<=n:
#         print(a)
#         a,b = b,a+b
# fib(150)

#Task_2
'''Дана последовательность целых чисел. Найти минимальное среди простых чисел и макс. среди чисел, не явл. простыми '''
# import random
# def is_prime(n):
#     if n < 2:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
# numbers = [random.randint(0, 100) for number in range(10)]
# numbers_prost = []
# numbers_ne_prost = []
# for num in numbers:
#     if is_prime(num):
#         numbers_prost.append(num)
#     else:
#         numbers_ne_prost.append(num)
# print(numbers)
# print(min(numbers_prost))
# print(max(numbers_ne_prost))

#Task_3
"""Дана последовательность целых чисел. Найти среднее арифм совершенных чисел и среднее геометр простых чисел"""
# import statistics
#
#
# def is_prime(n):
#     if n < 2:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
#
#
# print(is_prime(3))
#
#
# def is_sov(n):
#     sum_i = 0
#     for i in range(1, n):
#         if n % i == 0 and i < n:
#             sum_i += i
#     return sum_i == n
#
#
# print(is_sov(8129))
#
# numbers = [6, 12, 7, 28, 11, 496, 13, 17, 8128, 32, 34, 4577, 78,11,6]
# numbers_is_prime = []
# numbers_is_sov = []
# for num in numbers:
#     if is_prime(num):
#         numbers_is_prime.append(num)
#     if is_sov(num):
#         numbers_is_sov.append(num)
# print(numbers_is_prime)
# print(numbers_is_sov)
# print(sum(numbers_is_sov) / len(numbers_is_sov))
# print(statistics.geometric_mean(numbers_is_prime))


#Task_4 (5 tasks from ppt."Python for beginners - slide 13-14")

# import random
# def delit(n):
#     if n < 0:
#         n = abs(n)
#     count_i = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count_i += 1
#     return count_i
# numbers = [random.randint(-1000,1000) for n in range(20)]
# print(numbers)
# for num in numbers:
#     print(f"{num}:{delit(num)}")


# import random
# def sum_ch(n):
#     if n < 0:
#         n = str(abs(n))
#     sum_ch = 0
#     for i in str(n):
#         if int(i) % 2 == 0:
#             sum_ch += int(i)
#     return sum_ch
# numbers = [random.randint(-1000,1000) for n in range(5)]
# print(numbers)
# for number in numbers:
#     print(f"{number}:{sum_ch(number)}")


# import random
# def posled(n):
#     n = str(abs(n))
#     for i in range(0,len(n)-1):
#         if int(n[i]) >= int(n[i + 1]):
#             return False
#     return True
#
# numbers = [random.randint(-1000,1000) for n in range(10)]
# print(numbers)
# for num in numbers:
#     print(f"Строго возрастающая последовательность для {num}:{posled(num)}")


import random


# import math
#
#
# def prost(n):
#     if n < 0 or n == 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# numbers = [94, 2, 3, 5, 7, 12, 11, 13, 17, 100, 19, 23, 29, 31, 37, 41, 43, 4, 24, 25]
# print(numbers)
# numbers_prost = []
# for num in numbers:
#     if prost(num) is True:
#         numbers_prost.append(num)
# print(numbers_prost)
#
# for i in range(2, len(numbers_prost), 3):
#     print(f"Факториал {numbers_prost[i]}:{math.factorial(numbers_prost[i])}")

# def digit_1(N):
#     i = 0
#     while N > 0:
#         N = N // 10
#         i += 1
#     return i
#
#
# N = abs(int(input("Введите число ")))
# print(f"Количество разрядов числа {N}:{digit_1(N)}")
# print(f"Количество разрядов числа {int(N / 2)}:{digit_1(N / 2)}")
# if digit_1(N) == digit_1(N / 2):
#     print("Количество разрядов не изменилось")
# else:
#     print("Количество разрядов изменилось")


#Task_5 (3 tasks from ppt."Python for beginners - slide 36-37")
# def sum(n, kind=True):
#     n=str(n)
#     sum=0
#     for i in n:
#         if int(i)%2== (0 if kind else 1):
#             sum+=int(i)
#     return sum
# print(sum(int(input("Введите число ")),kind=True))


# Variant_1
# import random
# def max_13(n):
#    if n%13==0:
#        return n
# numbers=[random.randint(-1000,1000) for n in range(20)]
# print(numbers)
# numbers_13 = []
# for num in numbers:
#     if max_13(num) and num>0:
#         numbers_13.append(num)
# print(numbers_13)
# print(max(numbers_13))

# Variant_2:
# def max_13(*args):
#     max_13 = 0
#     for num in args:
#         if num % 13 == 0 and num > 0:
#             max_13 = max(max_13,num)
#     return max_13
# print(max_13(11, 12, 34, -13,13,39))


# import math
# def sq(x,y):
#     return x*y
# print(f"Площадь прямоугольника: {sq(4,5)}")
#
# def area(r):
#     pi= math.pi
#     return pi*r**2
# print(f"Площадь круга: {area(2)}")


'''Создайте функции cat_voice() and dog_voice(), которые выводят на экран 'Meow!' и 'Woof!' соответственно. 
Сделайте по одному вызову каждой из функций'''
# def cat_voice():
#     return "Meow!"
#
# print(cat_voice())
# def dog_voice():
#     return "Woof!"
# print(dog_voice())

'''Создайте функцию get_voice() которая возвращает передаваемый ей в качестве параметра текст c 
восклицательным знаком.
'''
# def get_voice(text:str):
#     return (text+'!')
# print(get_voice("kadfgnjjheogrjklfan"))
'''Создайте функцию, которая генерирует последовательность нечетных чисел в диапазоне от a до b (a и b включительно). 
Значения a и b должны передаваться в качестве параметров. Результирующая последовательность должна возвращаться в форме
 объекта list. Решите задание двумя способами - при помощи List Comprehension  и без него
'''
# def odd_sequence(a: int, b: int):
#     result = []
#     for i in range(a, b + 1):
#         if i % 2 != 0:
#             result.append(i)
#     return result
# print(odd_sequence(10,101))
#
# def seq(a:int,b:int):
#     return [i for i in range(a,b+1) if i%2 !=0]
# print(seq(10,101))

"""Создайте функцию is_cat_here(), которая принимает любое количество аргументов и проверяет есть ли строка 
'cat' среди них. Функция должна возвращать True, если такой параметр есть и False в обратном случае. 
Буквы в строке 'cat' могут быть как большие, так и маленькие.
"""
# def is_cat_here(*args:str):
#     for arg in args:
#         if 'cat'.upper() or 'cat'.lower() in arg:
#             return True
#         else:
#             return False
# print(is_cat_here("ergfcd,wefc,werf, 354cat"))

'''Создайте функцию is_item_here(item, *args), которая проверяет есть ли  item среди args.
 Функция должна возвращать True, если такой параметр есть и False в обратном случае.
'''
# def is_item_here(item,*args):
#     return item in args
# print(is_item_here(100,*(2342,1)))

"""Создайте функцию your_favorite_color() с позиционным параметром my_color и параметрами **kwargs, 
которая будет выводить на экран 'My favorite color is (значение my_color), what is your favorite color?', 
если в параметрах kwargs нет ключа color, и 'My favorite color is (значение my_color),
 but (значение по ключу color) is also pretty good!', если в параметрах kwargs ключ color присутствует"""
# def your_favorite_color(my_color,**kwargs):
#     if "color" in kwargs:
#         print(f"My favorite color is {my_color}, but {kwargs['color']} is also pretty good!'")
#     else:
#         print(f"My favorite color is {my_color}, what is your favorite color?")
# your_favorite_color("red",**{"col":"green"})
#     color = kwargs.get('color')
#     if color is None:
#         return (f"My favorite color is {my_color}, what is your favorite color?")
#     return (f"My favorite color is {my_color}, but {color} is also pretty good!")
# print(your_favorite_color("red",**{"1":'green'}))

"""Написать ф-цию, которая принимает один аргумент, который будет умножаться на заданное число"""
# def mult(x, y=2):
#     return x*y
# print(mult(10,3))

'''Написать программу, в которой с помощью функции sorted() и lambda-функции отсортировать слова в списке по второй букве '''
# l = ['apple', 'banana', 'carrot', 'dog', 'elephant']
# l_sorted = sorted(l,key =lambda x: x[1])
# print(l_sorted)

'''Написать программу, проверяющую, начинается ли заданная строка с заданного символа, с помощью lambda-функции'''
# text = "stgrethgbdfn"
# char = "s"
# starts_with = lambda text, char: True if text.startswith(char) else False
# print(starts_with(text, char))