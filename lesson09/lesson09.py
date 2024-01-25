
# --------------------------------------------------------файлы----------------------------------------------------------------------#
# файл - информация(текст, видео, аудио и т.д.)
# группы файлов для пайтона:
# * текстовые (это все то, что можно преобразовать к тексту, .txt, .pdf, .xlsx, .csv. .json и т.д.)
# * бинарные (это все то, что нельзя преобразовать к тексту без потери изначальных, .png, .mp4, .mp3 и т.д.)



# открывать !!!
# читать (получать информация)
# редактировать
# закрывать !!!

#
# f = open('file1.txt', 'r') # open(path, mode)
# data = f.read()  # получили весь текст файла (тип данных строковый)
# print(data, type(data))
# f.close()
#
# print("-------------------------------")
# f = open('file1.txt', 'r')
# first_line = f.readline() # первую строку (тип данных строковый)
# print(first_line, type(first_line))
# f.close()
#
#
# print("-------------------------------")
# f = open('file1.txt', 'r')
# lines = f.readlines() # list список строк файла
# print(lines, type(lines))
# f.close()



# f = open(r'C:\Users\Anastasia\Desktop\Groups\QA_328\python\lesson09\file1.txt', 'r') # open(path, mode)
# data = f.read()  # получили весь текст файла (тип данных строковый)
# print(data, type(data))
# f.close()


# #—------------------------------- Задача —--------------------------------#
# # дан файл, в каждой строке которого содержится стоимость товара.
# # Найти самый дорогой товар, самый дешевый товар и общую сумму покупки.
#
# # получить данные из файла
# f = open('cost_priducts.txt', 'r')
# cost_products = f.readlines()
# f.close()
#
# print(cost_products) #['1000\n', '500\n', '200\n', '30'] -> [1000,500,200,30]
# # # преобразовываем строки в числа
# for i, line in enumerate(cost_products):
#     cost_products[i] = int(line)
#
# # # # второй способ получить из списка строк список чисел
# # # from functools import * # - > filter, map, reduce ...
# # cost_products = list(map(lambda element: int(element), cost_products))
#
# print(cost_products)
# print(f'max cost: {max(cost_products)}')
# print(f'min cost: {min(cost_products)}')
# print(f'sum cost: {sum(cost_products)}')
# #

# #—------------------------------- Задача —--------------------------------#
# # дан файл, в каждой строке которого содержится фамилия человека.
# # Найти всех людей фамилия, которых начинается на К
# f = open('list_of_surnames.txt', 'r', encoding='utf-8')
# surnames = f.readlines()
# f.close()
# #print(surnames[0][0])
# print(surnames)
# for surname in surnames:
#      #print(surname)
#      if surname[0].lower() == 'к':
#           print(surname)



# # ---------------------запись данных в файл или редактирование---------------------------
# f = open('file_for_writing.txt', 'w')
# # все содержимое файла будет перезаписано
# f.write("Cat")# запись можно только строковой тип данных
# f.close()

# # лучше всего использоваться контекстный менеджер
# with open('file_for_writing.txt', 'r+') as f: # в ЛЮБОМ случае закроет файл
#     data = f.readline()
#     print('1 line: ', data)
#     data = f.readline()
#     print('2 line: ',data)
#     f.write('\nnew line') #  при режиме 'r+' в данном случае будет запись в конец строки
#     data = f.readline()
#     print('3 line: ', data)

#
# with open('file_for_writing.txt', 'w+') as f:
#     data = f.readline()
#     print('1 line: ', data)
#     data = f.readline()
#     print('2 line: ',data)
#     f.write('\nnew line') #  при режиме 'w+' будет перезапись всего файла
#     data = f.readline()
#     print('3 line: ', data)
#





# #Напишите функцию find_longest_string,
# # которая принимает на вход список строк и
# # возвращает самую длинную строку из списка.
# def find_longest_string(mylist):
#     max_length = 0
#     max_string = ''
#     for string in mylist:
#         if len(string) > max_length:
#             max_length = len(string)
#             max_string = string
#     return max_string
#
# mylist = ['5438888309', 'n75096', 'z6111111111111111111111111111111']
# s = find_longest_string(mylist)
# print(s)
#
#
#

#
#
# # #—------------------------------- Задача —--------------------------------#
# # # дан файл cost_products.txt, в каждой строке которого содержится стоимость товара.
# # # Записать в файл top3.txt топ 3 самых дорогих товара
#
# # полученение данных
# with open('cost_priducts.txt', 'r') as f:
#     cost_products = f.readlines()
#
# # преобразовали в список чисел
# cost_products = list(map(lambda num: int(num), cost_products))
#
# print(cost_products)
# cost_products.sort() #отсортировали
# print(cost_products)
#
# # сформировали данные для записи в top3.txt
# top3 = f"""Top 3:
# {cost_products[-1]}
# {cost_products[-2]}
# {cost_products[-3]}
# """
# print(top3)
#
# # запись в top3.txt
# with open('top3.txt', 'w') as f:
#     f.write(top3)





class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sleep(self):
        print(f"{self.name} sleep")
cat1 = Cat('Petya', 'black')
cat2 = Cat('Katya', "white")
#print()
cat1.sleep()
cat2.sleep()
