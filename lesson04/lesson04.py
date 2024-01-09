# ------------------------------ Коллекции ------------------------------------ #
# Коллекции - набор значений
# списки == массивы ! ИЗУЧИТЕ РАЗНИЦУ самостоятельно


# списки -> [1, 2.4, 'string', [1, 2, 3]], но чаще будет -> [1, 5, 6]
# строки -> 'string' - набор символов
# кортежи -> (1, 2.3, 5) - неизменяемый тип данных
# множества -> {5, 43, 3} - хранятся только уникальные значения
# словари -> {'key': 'value', 0: 1} - набор значений с ключами




# ------------------------------ кортежи ------------------------------------ #
# кортежи -> (1, 2.3, 5) - неизменяемый тип данных
# применяем для передачи аргументов в функцию
# элементы должны остаться неизменными

# # создание
# tuple_of_numbers = (1, 2)
# print(tuple_of_numbers[0])
# print(tuple_of_numbers)

# добавление - не доступна операция
# удаление - не доступна операция
# редактирование - не доступна операция
#tuple_of_numbers[0] = 4 #получим ошибку TypeError: 'tuple' object does not support item assignment

# # преобразование в список
# tuple_of_numbers = (1, 2)
# print(tuple_of_numbers)
# list_of_numbers = list(tuple_of_numbers)
# print(list_of_numbers)



# ------------------------------ множества ------------------------------------ #
# множества -> {5, 43, 3} - хранятся только уникальные значения
# когда нужно отобрать только уникальные значения

# # создание и обращение к элементам множества
# set_of_numbers = {1, 2}
# #print(set_of_numbers[0]) # обращение по индексу недоступно
# print(set_of_numbers)
# # for number in set_of_numbers:
# #     print(number)

# # добавление - добавить можно только уникальные значения
# set_of_numbers = {1, 2}
# set_of_numbers.add(3)
# set_of_numbers.add('1')
# set_of_numbers.add(2)
# print(set_of_numbers)
# set_of_numbers = {1, 2}
# set_of_numbers.update([2, 4]) # из списка берутся элементы и добавляются в множество
# print(set_of_numbers)


# # удаление - можно удалить только то, что есть
# set_of_numbers = {1, 2}
# set_of_numbers.remove(2)
# print(set_of_numbers)
# # set_of_numbers.remove(5) # KeyError

# редактирование - не доступна операция


# # ---------------------------------- Задача ---------------------------------------------------#
# # дан список элементов целых чисел, необходимо удалить дубликаты  и
# # показать список с отобранными числами расположенным в порядке по убыванию
# numbers = [1, 2, 32, -1, 0, 0, 1, 2, 32, -5] # -> [-5, -1, 0, 1, 2, 32]
# numbers = set(numbers)
# numbers = list(numbers)
# numbers.sort(reverse=True) #в порядке по убывание
# print(numbers)


# ---------------------------------- словари ---------------------------------------------------#
# словари -> {'key': 'value', 0: 1} - набор значений с ключами
# значение и ключ могут быть произвольного типа данных
# Но ключ должны быть уникальны


# # создание
# dictionary = {'key': 'value', 1: 'one', 2: 'two', '#': 32}
# print(dictionary)
# print(dictionary[1])
# print(dictionary['#'])

# # добавление -  доступна операция
# dictionary = {'key': 'value', 1: 'one', 2: 'two', '#': 32}
# dictionary[3] = 'three'
# dictionary.update({4: 'four'})
# print(dictionary)

# # удаление - доступна операция
# dictionary = {'key': 'value', 1: 'one', 2: 'two', '#': 32}
# dictionary.pop('key')
# print(dictionary)
# dictionary.popitem() # удаляет последнюю пару
# print(dictionary)


# # редактирование - доступна операция
# dictionary = {'key': 'value', 1: 'one', 2: 'two', '#': 32}
# print(dictionary)
# dictionary['#'] = 'this is #'
# dictionary.update({1: 'ONE'})
# print(dictionary)



# применение


# # ------------------------------------- Задача ------------------------------------------------#
# # пользователь вводит номер месяца, необходимо
# # отобразить кол-во дней (нельзя использовать
# # сторонние модули)
#
# number_of_month = 12
# # key -> номер месяца
# # value -> кол-во дней в этом месяце
# month_to_countDays = {1: 31, 2: 28, 3: 31, 4: 30} # и т.д.
#
# try: # сначала делаем
#     print(month_to_countDays[number_of_month])
# except: # сработает если была какая-либо ошибка
#     print("нет такого номера месяца")



# # # ------------------------------------Задача------------------------------#
# # # Дан список чисел, необходимо посчитать кол-во каждого уникального числа
# # # и сформировать из этих данных словарь
# numbers = [53, 43, 32, -5, 0, 5, 5, -5, 0, 5]
# # -> {53: 1, 43: 1, 32: 1, -5: 2, 0: 2, 5: 3}
# unique_numbers = set(numbers)
# dict_nums = dict()
# for num in unique_numbers:
#     #print(f"{num} -> {numbers.count(num)}")
#     dict_nums[num] = numbers.count(num)
# print(dict_nums)



# ------------------------------------Задача------------------------------#
# Дан список имен, необходимо найти самое популярное имя
# names = ['Masha', 'Yana', 'Masha', 'Ivan', 'Ivan', 'Ivan', 'Masha', 'Yana', 'Masha', 'Ivan']
# unique_names = set(names)
# dict_names = dict()
# print(unique_names)
# for name in unique_names:
#     dict_names[name] = names.count(name)
# max_count = max(dict_names.values())
# popular_names = []
#
# for key in dict_names:
#     #print(f"dict_names[{key}] = {dict_names[key]}")
#     if dict_names[key] == max_count:
#         popular_names.append(key)
#
# print(f"{dict_names}\n-----------------------")
# for name in popular_names:
#     print(f"popular name: {name}")




# #--------------------2----------------------#
# names = ['Ilia', 'Masha', 'Yana', 'Masha', 'Ivan', 'Ivan', 'Ivan', 'Masha', 'Yana', 'Masha', 'Ivan']
# unique_names = set(names)
# print(unique_names)
# max_count = -100 * 1000
# popular_names = []
# for name in unique_names: # найти максимальное кол-во упоминаний
#     if max_count <= names.count(name):
#         max_count = names.count(name)
#
# for name in unique_names: # отбираем все имена, которые подходят под max кол-во упом.
#     if max_count == names.count(name):
#         print(name, names.count(name))
#         popular_names.append(name)
# print(popular_names)




# # ------------------------------------Задача------------------------------#
# # Дан словарь, где ключ это тест-кейс, а значение - это ожидаемый результат
# # программа для перевода из метров в миллиметры
# #main program
# # программа для перевода из метров в миллиметры
# def main_program(value):
#     meters = value
#     result = meters * 1000
#     return result
#
#
#
# testCases = {('метр', 5): ('миллиметр', 5000),
#              ('метр', 0): ('миллиметр', 0),
#              ('метр', -1): ('миллиметр', False) }
#
#
# # test program
# for case in testCases:
#     if main_program(case[1]) == testCases[case][1]:
#         print("Тест успешный")
#     else:
#         print("Тест не успешный")






# -------------------------------- Строки ----------------------------------- #
# строки -> 'string' - набор символов
# '' "" '''''' """""" - они все равно сильны и все это строка\
#
print('''требуется перенос вот здесь
      и вот перенос с "" или '' такое не пройдет''')
"""
как еще один стиль оформления кода
"""

# операторы доступные для строк
print('склейка строк (конкатенация)', '1'+'2')
print('дублирование', '1' * 5)


# методы и функции по работе со строками

