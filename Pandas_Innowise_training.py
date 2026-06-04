from operator import index

import pandas as pd
from numpy.ma.extras import average

data = pd.read_csv(r"F:\Стажировка\Pandas practice\adult.data.csv")
# 1. Посчитайте, сколько мужчин и женщин (признак sex) представлено в этом датасете
sex_counts = data['sex'].value_counts()
print("Количество мужчин и женщин в датасете:")
print(sex_counts)

# 2. Каков средний возраст мужчин (признак age) по всему датасету?
male_age_avr = data.loc[data['sex'] == 'Male', 'age'].mean()
print(f"Средний возраст мужчин:{male_age_avr:.2f} лет")

# 3.Какова доля граждан Соединенных Штатов (признак native-country)?
mask = data['native-country'] == 'United-States'
total_count = len(data)
United_States_count = mask.sum()
United_States_share = United_States_count / total_count
print(f"Доля граждан Соединенных Штатов:{United_States_share:.2%}")

# 4-5. Рассчитайте среднее значение и среднеквадратичное отклонение возраста тех, кто получает более 50K в год (признак salary)
# и тех, кто получает менее 50K в год.
# Variant1:
avr_age_less_sal = data.loc[data['salary'] == '<=50K', 'age'].mean()
avr_age_more_sal = data.loc[data['salary'] == '>50K', 'age'].mean()
std_age_less_sal = data.loc[data['salary'] == '<=50K', 'age'].std()
std_age_more_sal = data.loc[data['salary'] == '>50K', 'age'].std()
print(f""
      f"\n Среднее значение возраста, кто получает <=50K: {avr_age_less_sal:.2f}"
      f"\n Среднее значение возраста,кто получает >50K: {avr_age_more_sal:.2f}"
      f"\n Cреднеквадратичное отклонение возраста, кто получает <=50K: {std_age_less_sal:.2f}"
      f"\n Cреднеквадратичное отклонение возраста, кто получает >50K: {std_age_more_sal:.2f}")
# Variant2:
income_age_stats = data.groupby('salary')['age'].agg(['mean', 'std'])
print(income_age_stats)

# 6. Правда ли, что люди, которые получают больше 50k, имеют минимум высшее образование?
# (признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)
education_level = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']
mask = data['salary'] == '>50K'
total_q_ty_more_50K = data[mask]['education'].count()
education_level_more_50K = data[mask]['education'].isin(education_level).sum()
education_level_share = education_level_more_50K / total_q_ty_more_50K
print(data[mask]['education'].isin(education_level).value_counts())
print(
    f"Утверждение неверно, доля людей с высшим образованием, которые получают больше 50k: {education_level_share:.2%}")

# 7. Выведите статистику возраста для каждой расы (признак race) и каждого пола. Используйте groupby и describe.
# Найдите таким образом максимальный возраст мужчин расы Asian-Pac-Islander.
# Variant1:
print(data.groupby(['race', 'sex']).agg({'age': 'max'}))
# Variant2:
print(data.groupby(['race', 'sex'])['age'].describe())
mask = (data['race'] == 'Asian-Pac-Islander') & (data['sex'] == 'Male')
mask_age = data[mask]['age'].max()
print(f"Максимальный возраст для мужчин расы Asian-Pac-Islander: {mask_age} лет")

# 8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак marital-status)?
# Женатыми считаем тех, у кого marital-status начинается с # Married (Married-civ-spouse, Married-spouse-absent или
# Married-AF-spouse), остальных считаем холостыми.
data_married_male = data[(data['sex'] == 'Male') & (data['marital-status'].str.contains('Married'))]
print(f" Количество всех женатых мужчин: {len(data_married_male)}")
data_married_rich_male = data_married_male[data_married_male['salary'] == '>50K']
print(f" Количество женатых мужчин, кто зарабатывает больше 50K: {len(data_married_rich_male)}")
data_unmarried_male = data[(data['sex'] == 'Male') & (~data['marital-status'].str.contains('Married'))]
print(f" Количество всех холостых мужчин: {len(data_unmarried_male)}")
data_unmarried_rich_male = data_unmarried_male[data_unmarried_male['salary'] == '>50K']
print(f" Количество холостых мужчин, кто зарабатывает больше 50K: {len(data_unmarried_rich_male)}")
married_share = len(data_married_rich_male) / len(data_married_male)
unmarried_share = len(data_unmarried_rich_male) / len(data_unmarried_male)
print(
    f" Доля зарабатывающих много (>50K) среди женатых - ({married_share:.2%})\n больше чем доля зарабатывающих много (>50K) среди холостых-({unmarried_share:.2%}.)")

# 9.Какое максимальное число часов человек работает в неделю (признак hours-per-week)?
# Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?
max_hours_week = data['hours-per-week'].max()
max_hours_week_people = data[data['hours-per-week'] == max_hours_week]
print(f"Максимальное число часов ({max_hours_week}) человек работает в неделю.")
print(f"Такое количество часов работает {len(max_hours_week_people)} человек.")
max_hours_week_rich_people = max_hours_week_people[max_hours_week_people['salary'] == '>50K']
print(f"Процент среди них зарабатывающих много:{len(max_hours_week_rich_people) / len(max_hours_week_people):.2%}")

# 10.Посчитайте среднее время работы (hours-per-week) зарабатывающих мало и много (salary) для каждой страны (native-country).
mask_low_salary = data['salary'] == '<=50K'
mask_high_salary = data['salary'] == '>50K'
print("Среднее время работы, зарабатывающих мало:")
print(data[mask_low_salary].groupby('native-country').agg({'hours-per-week': 'mean'}).sort_values(by='hours-per-week',
                                                                                                  ascending=False).reset_index())
print("Среднее время работы, зарабатывающих много:")
print(data[mask_high_salary].groupby('native-country').agg({'hours-per-week': 'mean'}).sort_values(by='hours-per-week',
                                                                                                   ascending=False).reset_index())

# 11.Сгруппируйте людей по возрастным группам young, adult, retiree, где:
# young соответствует 16-35 лет
# adult - 35-70 лет
# retiree - 70-100 лет
# Проставьте название соответсвтуещей группы для каждого человека в новой колонке AgeGroup
import numpy as np

conditions = [(data['age'] >= 16) & (data['age'] <= 35), (data['age'] > 35) & (data['age'] <= 70),
              (data['age'] > 70) & (data['age'] <= 100)]
groups = ['young', 'adult', 'retiree']
data['AgeGroup'] = np.select(conditions, groups, default='Группа не определена')
print(f"Группировка людей по возрастным группам:")
print(data[['age', 'AgeGroup']])

# 12-13. Определите количество зарабатывающих >50K в каждой из возрастных групп (колонка AgeGroup), а также выведите название
# возрастной группы, в которой чаще зарабатывают больше 50К (>50K)
print("Количество зарабатывающих >50K в каждой возрастной группе:")
count_by_group = data[data['salary'] == '<=50K'].groupby('AgeGroup')['salary'].count()
print(count_by_group)
print("Общее количество в каждой возрастной группе:")
total_by_group = data.groupby('AgeGroup')['salary'].count()
print(total_by_group)
share_by_group = (count_by_group.div(total_by_group) * 100).sort_values(ascending=False)
print(f"Название возрастной группы, в которой чаще зарабатывают больше 50К:{share_by_group.index[0]}")
print(f"В ней зарабатывает больше 50К: {share_by_group.iloc[0].round(2)}%.")

# 14. Сгруппируйте людей по типу занятости (колонка occupation) и определите количество людей в каждой группе.
# После чего напишите функциюю фильтрации filter_func, которая будет возвращать только те группы, в которых средний возраст
# (колонка age) не больше 40 и в которых все работники отрабатывают более 5 часов в неделю (колонка hours-per-week)
data['occupation'] = data['occupation'].replace('?', 'uknown')
print(data.groupby('occupation').size().sort_values(ascending=False))


def filter_func(group):
    avg_age_condition = group['age'].mean() <= 40
    hours_condition = group['hours-per-week'].min() > 5
    return avg_age_condition and hours_condition


filtered_data = data.groupby('occupation').filter(filter_func)
print("Отфильтрованные группы, удовлетворяющие двум условиям:")
print(filtered_data)
final_groups = filtered_data.groupby('occupation').size()
print("Количество людей в отфильтрованных группах:")
print(final_groups)

