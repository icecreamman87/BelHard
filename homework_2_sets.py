"""Задания на множества"""
# Task_6
text = 'укке'
print(len(set(text)))

# Task_7
list_1 = [-10, -13, -34, 12, 19, 101, 345, 8, 10, 19]
list_2 = [19, 34, -13, -10, 19, 25, 34, 345, 456, 567, 2, 456, 78, 101, 47]
set_1 = set(list_1)
set_2 = set(list_2)
print(set_1)
print(set_2)
list_3 = sorted(list(set_1.intersection(set_2)))
print(list_3)
list_4 = sorted(list(set_1.symmetric_difference(set_2)),reverse=True)
print(list_4)
list_5 =list_3 + list_4
print(list_5)

#Task_8
fig_1 = {5,4,3,7,3,1}
print(len(fig_1))
print(max(fig_1))
print(min(fig_1))

fig_2 = {4,4,7,2}
print(len(fig_2))
print(max(fig_2))
print(min(fig_2))

fig_3 ={9,9,9,9,9,9}
print(len(fig_3))
print(max(fig_3))
print(min(fig_3))

fig_4 = {1,0,0,0,0,0,1}
print(len(fig_4))
print(max(fig_4))
print(min(fig_4))
