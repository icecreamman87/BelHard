'''7. Напишите программу для решения квадратного уравнения. В процессе
поиска решения использовать обработку исключительных ситуаций.
'''


class CustomException(Exception):
    pass


a = input("Введите коэффициент a ")
b = input("Введите коэффициент b ")
c = input("Введите коэффициент c ")
try:
    a = float(a)
    b = float(b)
    c = float(c)
except Exception as e:
    raise CustomException("Введите числа")
if a == 0:
    print("Не квадратное уравнение, проверьте а")
else:
    print(f"a={a},b={b},c={c}")
    D = b ** 2 - 4 * a * c
    print(D)
    if D < 0:
        print("Решений нет")
    elif D == 0:
        x = -b / 2 * a
        print(f"Один корень: x={x}")
    if D > 0:
        x_1 = (-b + D ** 0.5) / 2 * a
        x_2 = (-b - D ** 0.5) / 2 * a
        print(f"Два корня:x_1={x_1},x_2={x_2}")
