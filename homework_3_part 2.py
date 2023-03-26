# Task_1
x = int(input("Введите отрезок x:"))
y = int(input("Введите отрезок y:"))
z = int(input("Введите отрезок z:"))
if x + y > z and x + z > y and y + z > x:
    print("Треугольник существует")
else:
    print("Треугольник не существует")
if not (x + y > z and x + z > y and y + z > x):
    print("Проверьте значения")
else:
    if x == y and y == z:
        print("Треугольник равносторонний")
    elif x != y and y != z and x != z:
        print("Треугольник разносторонний")
    elif (x == y and x != z and y != z) or (x == z and x != y and z != y) or (z == y and z != x and y != x):
        print("Треугольник равнобедренный")


# Task_2
a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
c = int(input("Введите число c:"))
list_1 =[a,b,c]
print(list_1)
print(f'max={max(list_1)},min={min(list_1)},avrg={sum(list_1)/len(list_1)}')
if min(list_1)>1 and min(list_1)//2:
    print(min(list_1))
else:
    print("Mин число меньше 1 или нечетное")
if max(list_1)>((min(list_1)+sum(list_1)/len(list_1))/2) or max(list_1)<(min(list_1)*sum(list_1)/len(list_1)):
    print(max(list_1))
else:
    print("Макс число не соответствует условиям")
if sum(list_1)/len(list_1)%3==0 and sum(list_1)/len(list_1)%2==0:
    print(sum(list_1)/len(list_1))
else:
    print("Среднее число не соответствует условиям")

# Task_3
year = int(input("Введите год:"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Год високосный")
else:
    print("Год невисокосный")


#Task_4
height = float(input("Введите рост,м:"))
weight = float(input("Введите вес,кг:"))
age = float(input("Введите возраст:"))
I = round(weight/height**2,2)
print(f'I={I}')
if (I<18.5 and age<45) or (I<22 and age>=45):
    print("Недостаточная масса тела")
elif (I>=18.5 and I<=24.99 and age<45) or (I>=22 and I<=26.99 and age>=45):
    print("Норма")
elif (I>=25 and I<=29.99 and age<45) or (I>=27 and I<=31.99 and age>=45):
    print("Избыточная масса тела")
else:
    print("Ожирение")


