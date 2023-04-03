"""В текстовом файле nums.txt хранятся вещественные числа. Вывести их на экран и вычислить количество"""

with open("nums.txt","r+") as f:
    data = f.readlines()
print(data)
print(len(data))
