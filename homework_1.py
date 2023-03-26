# Homework_1
# Task_1
a, b, c = 7, 'hello', 13.4
print(f' a={a}, b={b}, c={c}')

# Task_2
print(f'Идентификаторы:a={id(a)}, b={id(b)}, c={id(c)},Типы:a={type(a)}, b={type(b)}, c={type(c)}')

# Task_3
a = 'hello'
id_a = id(a)
id_b = id(b)
id_c = id(c)
print(id_a == id_b)
print(id_a == id_c)

# Task_4
A = B = C = 666

# Task_5
print(f'A={id(A)},B={id(B)}, C={id(C)}')

# Task_6
print(id(A) == id(B))
print(id(A) == id(C))
print(id(B) == id(C))
# Идентификаторы равны между собой, т.к. переменные имеют одно и то же значение

# Task_7
x, y, z = input("Введите переменную x: "), input("Введите переменную y: "), input("Введите переменную z : ")
print(f'Значения: x={x}, y={y}, z={z},Типы: x={type(x)}, y={type(y)}, z={type(z)}, Идентификаторы:x={id(x)}, y={id(y)}, z={id(z)}')
