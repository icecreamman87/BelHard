'''Создать файл, прочесть его, вывести количество строк файла.
Создать файл, заменить в этом файле строку.
Удалить строку из файла по ее индексу.
Вставить строку в указанную позицию файла.
'''
# Task_1
# with open("homework_5_1.txt","r+") as f:
#     data = f.readlines()
#     print(data)
#     print(len(data))

# Task_2 - в самом файле стройка не меняется!!!
# with open("homework_5_1.txt","r+") as f:
#     old_data = f.read()
#     print(old_data)
#     new_data = old_data.replace('dfb','Python')
#     print(new_data)

# Task_3
# with open("homework_5_1.txt", "r+") as f:
#     index = int(input("Введите индекс строки:"))
#     lines = f.readlines()
#     print(lines)
#     del lines[index]
# with open("homework_5_1.txt", "w") as f:
#     f.writelines(lines)
# with open("homework_5_1.txt", "r+") as f:
#     print(f.readlines())

# Task_4
# with open("homework_5_1.txt","r+") as f:
#     print(f.read())
#     print(f.tell())
#     print(f.seek(5))
#     print(f.write("Hello world"))
#     print(f.tell())
# with open("homework_5_1.txt","r+") as f:
#     print(f.read())
