# ----------------------------------------------------------------------#
# # круг из звездочек
# # Ввод: Пользователь вводит радиус круга или его диаметр.
# choice_user = input("""Пользователь вводит радиус круга(введите 1) или его диаметр(введите 2).""")
# if choice_user == '1':
#     r = int(input("""Пользователь вводит радиус круга"""))
# else:
#     d = int(input("""Пользователь вводит диаметр круга"""))
#     r = d//2
# side = '_*_'
# space = '___'
# space_with_side = 2 * space + r * side + 2 * space
# side_with_space = space + side + r * space + side + space # пробелы между звездами для скругления
# side_with_space2 = side + (r + 2) * space + side
# for i in range(1, r + 5):
#     if i == 1 or i == r + 4:
#         print(space_with_side)
#     elif i == 2 or i == r + 3:
#         print(side_with_space)
#     else:
#         print(side_with_space2)

# ----------------------------------------------------------------------#
#
# # дан  список
# # запрещено использовать sort, max, count, map преобразовывать список в другие типы тоже нельзя
# # найти элемент(ы) в списке, который повторяется дважды и более раз
# nums = [4, 67, 55, 2, 11, 32, 6, 11, 11, 2, 4]
# non_unique_nums = []
# for num in nums:
#     if nums.count(num) >= 2:
#         if not (num in non_unique_nums): #если нет числа в списке
#             non_unique_nums.append(num)
# print(non_unique_nums, "Количество элементов:", len(non_unique_nums))
#
# # дополнительная информация о кол-во повторений повторяющихся чисел
# # for num in non_unique_nums:
# #     print(num, "Количество повторений: ", nums.count(num))




# # ----------------------------------------------------------------------#
#
# # дан список
# # запрещено использовать sort, max, count, sum, map
# # # сформировать новый список, с положительными числами
# # ИДЕНТИЧНЫЕ ЗАДАНИЯ
# # # удалить из этого списка все отрицательные элементы
# # 1 часть
# nums = [-4, 67, -55, -44, 2, 0, 11, 32, -6, -11]
# positive_nums = []
# print(nums)
# for num in nums:
#     if num > 0:
#         positive_nums.append(num)
# print("positive:", positive_nums)
#
# # 2 часть
# i = 0
# while i < len(nums):
#     if nums[i] < 0:
#         nums.pop(i)  # удалили отрицательные числа
#         i -= 1
#     i += 1
# print(nums)

# # ----------------------------------------------------------------------#
# # задача
# # Напишите программу для вывода новогодней елочки из звездочек:
# #
# # Ввод: n = 4
# # Вывод:
# #    *
# #   ***
# #  *****
# # *******
# #   |||
# n = 4
# y = "*"
# e = "|"
# print()
# d = 1 # кол-во звезд в каждой строке
# for i in range(1, n + 1):
#     print(" " * (n-i+1), y * d)
#     d += 2 # увеличиваем на 2
# for i in range(1):
#     print(" " * 3, e * 3)

#
# #
# # --------- 2 ----------------
#
# n = int(input("введите количество строк "))
#
# m = "*"
#
# s = " "
#
# z = "|||"
#
# for i in range(1, n+1):
# #s*(n-i) - постали сколько надо пробелов
# #  (m * i) + m * (i-1)- кол-во звезд
# #  номер строки + (номер строки -1) # 2 + 1
# # 3+2
#     print(s*(n-i) + (m * i) + m * (i-1))
#
# print (s*(n-2) + z)




# # # ----------------------------------------------------------------------#
# # дан  список
# # # найти  все элементы в этом списке , у которых индекс и значение совпадают. Исходный список нельзя менять
# nums = [0, 1, 67, 3, -55, 2, 11, 32, 6, 11]
# print(nums)
# answer = []
# for num in nums:
#      if nums.index(num) == num:
#         answer.append(num) #print(num)
# print(answer)






# # ------------------------------ срезы ---------------------------------- #
# # срезы -кусочек(часть) коллекции от и до
# # работает для всех коллекций к которым можно обратиться по индексу
# nums = [55, 33, 44, 22]
# # start : end(не включается) : step
# print(nums[0:2])
# print(nums[::]) # nums[::] -> nums
# print(nums[1:])
# print(nums[:3])
# print(nums[1::2])
# print(nums[::-1]) # развернуть список

# # ---------------------------Задача--------------------------------- #
# # дана строка, в которой содержатся только цифры
# # удалить все нули из строки и оставить только
# # ввод 1002001
# # вывод 121
# test_string = "1002001"
# print(test_string.replace('0',''))

# # ---------------------------Задача--------------------------------- #
# # дана строка, в которой содержатся только цифры
# # разделить строку на две равные части и склеить их,
# # предварительно поменяв местами
# # ввод 102201
# # вывод 201102
# # ввод 10201
# # вывод 01210
# test_string = "102201"
# if len(test_string) % 2 == 0:
#     m = len(test_string) // 2 # середина
#     part1 = test_string[:m]
#     part2 = test_string[m:]
#     print(part1, part2)
#     result = part2 + part1
# else:
#     m = len(test_string) // 2  # середина
#     part1 = test_string[:m]
#     part2 = test_string[m+1:]
#     m = test_string[m]
#     print(part1, m, part2)
#     result = part2 + m + part1
# print(result)







#—------------------------------- Задача —--------------------------------#
# Дан список строк такого формата :
# "Имя: Яблоки, рублей за кг: 25, всего кг: 30”,
# "Имя: Груши: рублей за кг: 50, всего кг: 100”,
# "Имя: Молоко, рублей за шт: 55, всего шт: 200”
#
#
# Сформировать словарь с товарами.
# Выведите на экран все товары,
# цена которых не превышает 1000 рублей,
# а текущий остаток не менее 10 единиц товара (кг шт и т.д.).
# Проверку на правильность формата строки делать не нужно
#

#"Имя: Яблоки, рублей за кг: 25, всего кг: 30”,
# "Имя: Груши: рублей за кг: 50, всего кг: 100”,
# [{Имя: Яблоки, рублей за кг: 25, всего кг: 30},
# {},
# {},
# ...]
test_strings = [
"Имя: Яблоки, рублей за кг: 25, всего кг: 30",
"Имя: Груши, рублей за кг: 50, всего кг: 100",
"Имя: Молоко, рублей за шт: 55, всего шт: 200"]
list_products = []
for i, el in enumerate(test_strings):
    product = {}
    # Ищем "Имя"
    name = test_strings[i][:3] #test_string[0] - это строка в данном случае
    start_i_name = test_strings[i].find(' ')+1
    end_i_name = test_strings[i].find(',')
    # Ищем значение имени
    name_product = test_strings[i][start_i_name:end_i_name]# ищем имя продукта
    product[name] = name_product
   # print(product)

    # Ищем "рублей за..."
    test_string = test_strings[i][end_i_name+2:]
    end_i_price = test_string.find(':')
    name_price = "рублей за единицу товара"
    # Ищем значение "рублей за..."
    test_string = test_string[end_i_price+2:]
    end_i_price = test_string.find(',')
    price = test_string[:end_i_price]
    product[name_price] = int(price)
    #print(product)

     # Ищем "всего..."
    test_string = test_string[end_i_price + 2:]
    end_i_count = test_string.find(':')
    # test_string[:end_i_count]
    name_count = "всего единиц товара"
    # Ищем значение "всего..."
    test_string = test_string[end_i_count + 2:]
    end_i_count = test_string.find(',')
    count = test_string[:end_i_price+1]
    product[name_count] = int(count)
    #print(product)

    # полученный словарь product добаваляем в список товаров
    list_products.append(product)
#print(list_products)

for product in list_products:
    finally_price = product['рублей за единицу товара'] * product['всего единиц товара']
    if finally_price <= 1000 and product['всего единиц товара'] >= 10:
        print(product['Имя'], ' - итоговая цена:', finally_price, 'всего единиц товара:',product['всего единиц товара'] )