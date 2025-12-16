import random
import numpy as np

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

# 3.Построить прямое произведение массивов (все комбинации с каждым элементом). На вход подается двумерный массив
# Variant 1
import itertools


def cartesian_product_of_arrays(two_d_arr):
    return np.array(list(itertools.product(*two_d_arr)))


arr = np.random.randint(-10, 10, (2, 2))
combinations = cartesian_product_of_arrays(arr)
print(f"Двумерный массив_вариант_1:{arr}")
print(f"Возможные комбинации_вариант_1:{combinations}")


# Variant 2
def cartesian_product_iterative(two_d_array):
    if isinstance(two_d_array, np.ndarray):
        two_d_array = two_d_array.tolist()
    if not two_d_array:
        return [[]]
    result = [[]]
    for arr in two_d_array:
        new_result = []
        for current_combination in result:
            for element in arr:
                new_result.append(current_combination + [element])
        result = new_result
    return result


combinations_2 = np.array(cartesian_product_iterative(arr))
print(f"Возможные комбинации_2 вариант: {combinations_2}")

# 4. Даны 2 массива A (8x3) и B (2x2). Найти строки в A, которые содержат элементы из каждой строки в B,
# независимо от порядка элементов в B

import numpy as np


def rows_match(A, B):
    result = []
    for row_a in A:
        if all(set(row_b).issubset(set(row_a)) for row_b in B):
            result.append(row_a)
    return np.array(result) if result else np.array([])


A = np.random.randint(0, 5, (8, 3))
B = np.random.randint(0, 5, (2, 2))
result_rows = rows_match(A, B)

print(f"Массив A:\n{A}")
print(f"Массив B:\n{B}")
print(f"Строки A, которые  содержат элементы из B:\n{result_rows}")

# 5. Дана 10x3 матрица, найти строки из неравных значений (например строка [2,2,3] остается, строка [3,3,3] удаляется)
matrix = np.random.randint(0, 3, (10, 3))
print(f"Матрица 10x3:\n{matrix}")
different_rows = [row for row in matrix if len(set(row)) > 1]
print("\nСтроки, где не все элементы одинаковые:")
result = np.array(different_rows)
print(result)
print(f"\nОсталось строк: {len(result)} из {len(matrix)}")

# 6. Дан двумерный массив. Удалить те строки, которые повторяются
arr_2_d = np.random.randint(0, 5, (20, 3))
print(f"Двумерный массив: {arr_2_d}")
unique_arr = np.unique(arr_2_d, axis=0)
print(f"Уникальные строки :\n{unique_arr}")
print(f"Количество строк-дубликатов:{len(arr_2_d) - len(unique_arr)}")


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
print(element_prod)

# Variant 2
matrix = np.random.randint(-10, 10, (4, 3))
print(matrix)


def diagonal_nonzero_product(matrix):
    n = min(matrix.shape[0], matrix.shape[1])
    diag_elements = np.array([matrix[i, i] for i in range(n)])
    print(diag_elements)
    nonzero_elements = diag_elements[diag_elements != 0]
    product = np.prod(nonzero_elements)
    return product


element_prod = diagonal_nonzero_product(matrix)
print(element_prod)


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
def multisets_equal(x, y):
    if len(x) != len(y):
        return False
    return np.array_equal(np.sort(x), np.sort(y))


x_np = np.array([36, 39, 38, 37])
y_np = np.array([36, 37, 38, 39])
z_np = np.array([100, 36, 39, 37])
print("Векторы NumPy:")
print(f"x = {x_np}, y = {y_np} -> {multisets_equal(x_np, y_np)}")
print(f"x = {x_np}, z = {z_np} -> {multisets_equal(x_np, z_np)}")


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
print(max_elem(x))


# Variant 2
def max_elem(x):
    mask = x[:-1] == 0
    if not mask.any():
        return None
    return x[1:][mask].max()


x = np.array([-10, 0, 123, 0, 49, -234, 0, 435, 0, 124])
print(x)
print(max_elem(x))


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


x = [2, 2, 2, 3, 3, 3, 5]
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
def rle(x):
    if len(x) == 0:
        return np.array([]), np.array([])
    change_positions = np.where(x[1:] != x[:-1])[0] + 1
    run_starts = np.concatenate(([0], change_positions))
    run_ends = np.concatenate((change_positions, [len(x)]))
    values = x[run_starts]
    counts = run_ends - run_starts
    return values, counts


x = np.array([2, 2, 2, 3, 3, 3, 5])
values, counts = rle(x)
print(f"Исходный вектор: {x}")
print(f"Кортеж: ({values}, {counts})")

# Задача 5: Даны две выборки объектов - X и Y. Вычислить матрицу евклидовых расстояний между объектами.
# Сравните с функцией scipy.spatial.distance.cdist по скорости работы.
# Variant1:
import math
import time


def euclidean_distance_1(X, Y):
    m = len(X)
    n = len(Y)
    if m == 0 or n == 0:
        return []
    dim = len(X[1])
    dist_matrix = [[0.0] * n for _ in range(m)]
    for i in range(m):
        xi = X[i]
        for j in range(n):
            yj = Y[j]
            squared_sum = 0.0
            for k in range(dim):
                diff = xi[k] - yj[k]
                squared_sum += diff * diff
            dist_matrix[i][j] = math.sqrt(squared_sum)
    return dist_matrix


X = [[3, -8, -8], [-4, 7, 9]]
Y = [[0, -9, -10], [7, 5, -1]]
print(f"Списки X и Y:\n X={X} \n Y={Y}")
print("Матрица евклидовых расстояний:")
dist = euclidean_distance_1(X, Y)
for row in dist:
    print([val for val in row])


# Variant2:
def euclidean_distance_2(X, Y):
    X = np.asarray(X)
    Y = np.asarray(Y)
    if X.ndim != 2 or Y.ndim != 2:
        raise ValueError("X и Y должны быть двумерными массивами")
    if X.shape[1] != Y.shape[1]:
        raise ValueError("X и Y должны иметь одинаковое количество столбцов")
    diff = X[:, np.newaxis, :] - Y[np.newaxis, :, :]
    squared_diff = diff ** 2
    squared_dist = np.sum(squared_diff, axis=2)
    dist_matrix = np.sqrt(squared_dist)
    return dist_matrix


np.random.seed(123)
X = np.random.randint(-10, 10, (2, 3))
Y = np.random.randint(-10, 10, (2, 3))
print(f"Массивы X и Y:\n X={X} \n Y={Y}")
dist = euclidean_distance_2(X, Y)
print(f"Матрица евклидовых расстояний:\n{dist}")

# Variant 3
from scipy.spatial.distance import cdist


def euclidean_distance_3(X, Y, metric='euclidean'):
    X = np.asarray(X)
    Y = np.asarray(Y)
    if X.ndim != 2 or Y.ndim != 2:
        raise ValueError("X и Y должны быть двумерными массивами")
    if X.shape[1] != Y.shape[1]:
        raise ValueError("X и Y должны иметь одинаковое количество столбцов")
    dist_matrix = cdist(X, Y, metric=metric)
    return dist_matrix


np.random.seed(123)
X = np.random.randint(-10, 10, (2, 3))
Y = np.random.randint(-10, 10, (2, 3))
print(f"Массивы X и Y:\n X={X} \n Y={Y}")
dist = euclidean_distance_3(X, Y)
print(f"Матрица евклидовых расстояний:\n{dist}")

start_1 = time.perf_counter()
euclidean_distance_1(X, Y)
end_1 = time.perf_counter()
time_1 = end_1 - start_1
print(f" Время решения с python: {time_1:.6f} секунд")
start_2 = time.perf_counter()
euclidean_distance_2(X, Y)
end_2 = time.perf_counter()
time_2 = end_2 - start_2
print(f" Время решения с numpy: {time_2:.6f} cекунд")
start_3 = time.perf_counter()
euclidean_distance_3(X, Y)
end_3 = time.perf_counter()
time_3 = end_3 - start_3
print(f" Время решения с cdist : {time_3:.6f} cекунд")

# 1.Просмотрите файл cereal.csv. Этот файл содержит количества калорий для различных марок хлопьев.
# Загрузите данные из файла и сохраните их как calorie_stats.
import numpy as np

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
