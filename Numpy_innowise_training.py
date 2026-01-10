import random
import numpy as np
import itertools
import math
import time
from scipy.spatial.distance import cdist

# 1. Дан случайный массив, поменять знак у элементов, значения которых между 3 и 8
# Variant_1
ave_1 = np.random.randint(-10, 10, 20)
print(f"Исходный массив_вариант_1:{ave_1}")
for i in range(len(ave_1)):
    if 3 <= ave_1[i] <= 8:
        ave_1[i] = -ave_1[i]
print(f"Измененный массив_вариант_1:{ave_1}")
# Variant_2
ave_1 = np.random.randint(-10, 10, 20)
print(f"Исходный массив_вариант_2:{ave_1}")
mask = (ave_1 >= 3) & (ave_1 <= 8)
ave_1[mask] = -ave_1[mask]
print(f"Измененный массив_вариант_2:{ave_1}")
print("------------------------")
# 2. Заменить максимальный элемент случайного массива на 0
# Variant_1
ave_2 = np.random.randint(-5, 50, 10)
print(f"Исходный массив_вариант_1:{ave_2}")
for i in range(len(ave_2)):
    if ave_2[i] == max(ave_2):
        ave_2[i] = 0
print(f"Измененный массив_вариант_1:{ave_2}")
# Variant_2
ave_2 = np.random.randint(-5, 50, 10)
print(f"Исходный массив_вариант_2:{ave_2}")
mask = ave_2 == np.max(ave_2)
ave_2[mask] = 0
print(f"Измененный массив_вариант_2:{ave_2}")
print("------------------------")


# 3.Построить прямое произведение массивов (все комбинации с каждым элементом). На вход подается двумерный массив
# Variant 1
def cartesian_product_of_arrays(two_d_arr):
    return np.array(list(itertools.product(*two_d_arr)))


arr = np.random.randint(-10, 10, (2, 2))
combinations = cartesian_product_of_arrays(arr)
print(f"Двумерный массив_вариант_1:{arr}")
print(f"Возможные комбинации_вариант_1:{combinations}")
# Variant 2
data = np.random.randint(-10, 10, (2, 2))
print(f"Двумерный массив_вариант_2:{data}")
grids = np.meshgrid(*data)
flat_grids = [x.ravel() for x in grids]
ave = np.column_stack(flat_grids)
print(f"Возможные комбинации_вариант_2:{ave}")
print("------------------------")
# 4. Даны 2 массива A (8x3) и B (2x2). Найти строки в A, которые содержат элементы из каждой строки в B,
# независимо от порядка элементов в B
A = np.random.randint(0, 10, (8, 3))
B = np.array([[1, 2],
              [3, 4]])
print("Массив A:\n", A)
print("Массив B:\n", B)
mask_1 = np.isin(A, B[0]).any(axis=1)
mask_2 = np.isin(A, B[1]).any(axis=1)
mask_3 = mask_1 & mask_2
data = A[mask_3]
print(f"Cтроки в A, которые содержат элементы из каждой строки в B:{data}")
print("------------------------")
# 5. Дана 10x3 матрица, найти строки из неравных значений (например строка [2,2,3] остается, строка [3,3,3] удаляется)
Z = np.random.randint(0, 5, (10, 3))
print(f"Исходная матрица:{Z}")
first_col = Z[:, 0:1]
mask = np.any(Z != first_col, axis=1)
print(f"Cтроки из неравных значений:{Z[mask]}")
print("------------------------")
# 6. Дан двумерный массив. Удалить те строки, которые повторяются
Z = np.array([[3, 4, 5], [1, 1, 2], [1, 2, 3], [1, 1, 2], [1, 4, 5]])
u, indexes = np.unique(Z, axis=0, return_index=True)
indexes = np.sort(indexes)
result = Z[indexes]
print(result)
print("------------------------")


# Задача 1: Подсчитать произведение ненулевых элементов на диагонали прямоугольной матрицы.
# Variant_1
def diagonal_product(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    n = min(rows, cols)
    diag_elements = []
    for i in range(n):
        diag_elements.append(matrix[i][i])
    print(f"Диагональные элементы: {diag_elements}")
    nonzero_elements = [x for x in diag_elements if x != 0]
    print(f"Ненулевые элементы: {nonzero_elements}")
    product = 1
    for elem in nonzero_elements:
        product *= elem
    return product


matrix = [
    [1, 3, 8],
    [-5, 0, 0],
    [-9, 0, 8],
    [-23, 0, 0]
]
element_prod = diagonal_product(matrix)
print(f"Произведение ненулевых элементов_ вариант_1: {element_prod}")
# Variant 2
Z = np.array([
    [1, 3, 8],
    [-5, 0, 0],
    [-9, 0, 8],
    [-23, 0, 0]])
d = np.diag(Z)
mask = d != 0
result = np.prod(d[mask])
print(f"Произведение ненулевых элементов_ вариант_2: {result}")
print("------------------------")


# Задача 2: Даны два вектора x и y. Проверить, задают ли они одно и то же мультимножество.
# Variant_1
def multisets_equal(x, y):
    if len(x) != len(y):
        return False
    return sorted(x) == sorted(y)


x = [36, 39, 38, 37]
y = [36, 37, 38, 39]
z = [100, 36, 39, 37]
print("Векторы:")
print(f"x = {x}, y = {y} -> {multisets_equal(x, y)}")
print(f"x = {x}, z = {z} -> {multisets_equal(x, z)}")
# Variant_2
x = np.array([36, 39, 38, 37])
y = np.array([36, 37, 38, 40])
x_sort = np.sort(x)
y_sort = np.sort(y)
if np.all(x_sort == y_sort):
    print(f"вектор {x} одно мультимножество с {y}")
else:
    print("Разные мультимножества")
print("------------------------")


# Задача 3: Найти максимальный элемент в векторе x среди элементов, перед которыми стоит ноль.
# Variant 1
def max_elem(x):
    if not x or len(x) < 2:
        return None
    elements = []
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            elements.append(x[i])
    if not elements:
        return None
    return max(elements)


x = [-10, 0, 123, 0, 49, -234, 0, 435, 0, 124]
print(f"Максимальный элемент в векторе x среди элементов, перед которыми стоит ноль_вариант_1:{max_elem(x)}")
# Variant 2
x = np.array([-10, 0, 123, 0, 49, -234, 0, 435, 0, 124])
mask = x[:-1] == 0
if np.any(mask):
    print(f"Максимальный элемент в векторе x среди элементов, перед которыми стоит ноль_вариант_2:{max(x[1:][mask])}")
else:
    print(f"Подходящих элементов нет")
print("------------------------")


# Задача 4: Реализовать кодирование длин серий (Run-length encoding). Для некоторого вектора x необходимо вернуть кортеж из двух векторов
# одинаковой длины. Первый содержит числа, а второй - сколько раз их нужно повторить.
# Например, для x = np.array([2, 2, 2, 3, 3, 3, 5]) ответ (np.array([2, 3, 5]), np.array([3, 3, 1])).
# Variant1
def rle(x):
    if not x:
        return [], []
    values = []
    counts = []
    current_value = x[0]
    current_count = 1
    for value in x[1:]:
        if value == current_value:
            current_count += 1
        else:
            values.append(current_value)
            counts.append(current_count)
            current_value = value
            current_count = 1
    values.append(current_value)
    counts.append(current_count)
    return values, counts


x = [22, 22, 22, 33, 33, 33, 51, 51, -1]
values, counts = rle(x)
print(f"Исходный вектор: {x}")
print(f"Кортеж: ({values}, {counts})")
# Variant 2
from itertools import groupby


def rle(x):
    values = []
    counts = []
    for key, group in groupby(x):
        values.append(key)
        counts.append(len(list(group)))
    return values, counts


x = [22, 22, 22, 33, 33, 33, 51, 51, -1]
values, counts = rle(x)
print(f"Исходный вектор: {x}")
print(f"Кортежи: ({values}, {counts})")
# Variant 3
x = np.array([22, 22, 22, 33, 33, 33, 51, 51, -1])
mask = x[:-1] != x[1:]
i = np.where(mask)[0]
i = np.append(i, len(x) - 1)
run_values = x[i]
run_counts = np.diff(np.append(-1, i))
print(f"Исходный вектор: {x}")
print(f"Значения:({run_values}, {run_counts})")
print("------------------------")


# Задача 5: Даны две выборки объектов - X и Y. Вычислить матрицу евклидовых расстояний между объектами.
# Сравните с функцией scipy.spatial.distance.cdist по скорости работы.
def distances_numpy(X, Y):
    sum_x = np.sum(X ** 2, axis=1)[:, np.newaxis]
    sum_y = np.sum(Y ** 2, axis=1)
    dists_sq = sum_x - 2 * (X @ Y.T) + sum_y
    return np.sqrt(dists_sq)


def distances_python(X, Y):
    dists = []
    for row_x in X:
        row_dists = []
        for row_y in Y:
            result = 0
            for a, b in zip(row_x, row_y):
                result += a ** 2 - 2 * a * b + b ** 2
            row_dists.append(math.sqrt(result))
        dists.append(row_dists)
    return dists


X = np.random.rand(200, 100)
Y = np.random.rand(200, 100)
X_list = X.tolist()
Y_list = Y.tolist()
result_numpy = distances_numpy(X, Y)
print("Результат функции (NumPy):")
print(result_numpy)
start_numpy = time.perf_counter()
distances_numpy(X, Y)
end_numpy = time.perf_counter()
time_numpy = end_numpy - start_numpy
print(f" Время решения с numpy: {time_numpy:.6f} cекунд")
result_python = distances_python(X_list, Y_list)
print("Результат функции python):")
print(result_python)
start_python = time.perf_counter()
distances_python(X_list, Y_list)
end_python = time.perf_counter()
time_python = end_python - start_python
print(f" Время решения с python: {time_python:.6f} cекунд")
result_cdist = cdist(X, Y)
print("Результат функции (cdist):")
print(result_cdist)
start_cdist = time.perf_counter()
cdist(X, Y)
end_cdist = time.perf_counter()
time_cdist = end_cdist - start_cdist
print(f" Время решения с cdist: {time_cdist:.6f} cекунд")
print(f"\nNumPy быстрее чем python в: {time_python / time_numpy:.6f} раз!")
print("------------------------")
# 1.Просмотрите файл cereal.csv. Этот файл содержит количества калорий для различных марок хлопьев.
# Загрузите данные из файла и сохраните их как calorie_stats.
calorie_stats = np.loadtxt(r"F:\Стажировка\Numpy practice\cereal.csv", delimiter=",")
print(calorie_stats)
# 2.В одной порции CrunchieMunchies содержится 60 калорий. Насколько выше среднее количество калорий у ваших конкурентов?
# Сохраните ответ в переменной average_calories и распечатайте переменную в терминале
CrunchieMunchies_cal = 60
average_calories = np.mean(calorie_stats)
diff_calories = average_calories - CrunchieMunchies_cal
print(f"Cреднее количество калорий у конкурентов: {average_calories:.2f}")
print(f"Cреднее количество калорий у конкурентов выше на {diff_calories:.2f}")
# №3.Корректно ли среднее количество калорий отражает распределение набора данных? Давайте отсортируем данные и посмотрим.
# Отсортируйте данные и сохраните результат в переменной calorie_stats_sorted. Распечатайте отсортированную информацию
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)
# 4.Похоже, что большинство значений выше среднего. Давайте посмотрим, является ли медиана наиболее корректным показателем набора данных.
# Вычислите медиану набора данных и сохраните свой ответ в median_calories.
# Выведите медиану, чтобы вы могли видеть, как она сравнивается со средним значением.
median_calories = np.median(calorie_stats)
print(f"Медиана калорий у конкурентов:{median_calories:.2f}")
# 5.В то время как медиана показывает, что по крайней мере половина наших значений составляет более 100 калорий,
# было бы более впечатляюще показать, что значительная часть конкурентов имеет более высокое количество калорий, чем CrunchieMunchies.
# Рассчитайте различные процентили и распечатайте их, пока не найдете наименьший процентиль, превышающий 60 калорий.
# Сохраните это значение в переменной nth_percentile.
nth_percentile = None
for p in range(101):
    value_at_p = np.percentile(calorie_stats, p)
    print(f"{p}-й процентиль: {value_at_p}")
    if value_at_p > CrunchieMunchies_cal:
        nth_percentile = p
        break
print(f"Наименьший процентиль, превышающий 60 калорий:{nth_percentile}")
# 6.Хотя процентиль показывает нам, что у большинства конкурентов количество калорий намного выше,
# это неудобная концепция для использования в маркетинговых материалах.
# Вместо этого давайте подсчитаем процент хлопьев, в которых содержится более 60 калорий на порцию.
# Сохраните свой ответ в переменной more_calories и распечатайте его
more_than_60 = np.sum(calorie_stats > 60)
total_brands = len(calorie_stats)
more_calories = (more_than_60 / total_brands) * 100
print(f"Процент хлопьев, в которых содержится более 60 калорий по сравнению с CrunchieMunchies : {more_calories:.2f}%")
# 7. Это действительно высокий процент. Это будет очень полезно, когда мы будем продвигать CrunchieMunchies.
# Но один вопрос заключается в том, насколько велики различия в наборе данных? Можем ли мы сделать обобщение, что в большинстве
# злаков содержится около 100 калорий или разброс еще больше?
# Рассчитайте величину отклонения, найдя стандартное отклонение, Сохраните свой ответ в calorie_std и распечатайте на терминале.
# Как мы можем включить эту ценность в наш анализ?
calorie_std = np.std(calorie_stats)
print(
    f"Стандартное отклонение конкурентов:{calorie_std:.2f}, что означает разброс калорий на рынке в {calorie_std:.2f} калорий")
score = (average_calories - CrunchieMunchies_cal) / calorie_std
min_calorie_stats = np.min(calorie_stats)
max_calorie_stats = np.max(calorie_stats)
range_calorie_stats = np.max(calorie_stats) - np.min(calorie_stats)
print(
    f"CrunchieMunchies ниже среднего значения конкурентов на: {score:.2f} стандартных отклонений или {diff_calories:.2f} калорий ")
print(f"Размах значений: {range_calorie_stats} калорий")
values, counts = np.unique(calorie_stats, return_counts=True)
max_index = np.argmax(counts)
print(f"Количество калорий, встречающееся чаще всего: {values[max_index]}, встречается {counts[max_index]} раз")
# 8. Напишите короткий абзац, в котором кратко изложите свои выводы и то, как, по вашему мнению,
# эти данные могут быть использованы в интересах Mycrunch при маркетинге CrunchieMunchies.
print(
    f"Наши данные демонстрируют, что CrunchieMunchies превосходит своих конкурентов по калорийности. Для этого обратимся к статистике:"
    f"\n 1.При {CrunchieMunchies_cal} калориях на порцию наш продукт содержит на {diff_calories:.2f} калорий меньше,"
    f"\n чем в среднем по рынку ({average_calories:.2f} калорий),что составляет {score:.2f} стандартных отклонения. "
    f" \n Медиана не сильно отличается от среднего и составляет {median_calories:.2f}, что говорит об отсутствии сильного перекоса в данных."
    f"\n 2. {more_calories:.2f}% всех конкурентов имеют калорийность выше {CrunchieMunchies_cal} калорий, "
    f"\n а само распределение калорийности хлопьев на рынке (со стандартным отклонением {calorie_std:.2f} калории) показывает "
    f"\n значительный разброс, при этом большинство брендов сконцентрированы вокруг {values[max_index]} калорий. "
    f"\n Этим же значением является и размах калорий: {range_calorie_stats}.  "
    f"\n 3.CrunchieMunchies попадает в нижние {nth_percentile}% по калорийности среди своих конкурентов. "
    f"\n Таким образом, CrunchieMunchies один из самых низкокалорийных вариантов на рынке.")
