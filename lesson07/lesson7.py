# ----------------------------------функции-------------------------------------------- #
# функция == действие
# это сохраненный алгоритм
# from turtle import *
# from time import sleep
#
# # define - объявлять
# # params:
# # a - сторона треугольника (параметр или аргумент функции)
# # color_side - цвет стороны одного треугольника
# def draw_triangle(a, color_side='black'): # алгоритм рисования треугольника
#     color(color_side)
#     forward(a)
#     left(120)
#     forward(a)
#     left(120)
#     forward(a)
#     left(120)
#
# side_user = 100
# # вызов функции
# draw_triangle(side_user)#color_side='black'
#
# left(60)
#
# # алгоритм рисования треугольника
# draw_triangle(side_user)# вызов функции color_side='black'
#
# right(60)
# forward(side_user)
# left(60)
#
# # алгоритм рисования треугольника
# draw_triangle(side_user)# вызов функции color_side='black'
#
#
# left(60)
# forward(side_user)
# right(30)
#
# draw_triangle(side_user, 'blue')# вызов функции
# sleep(10)


# ----------------------------- Задача ----------------------------------#
# # функция проверки существования треугольника
# def is_valid_triangle(a, b, c): # проверяет существует ли треугольник
#     if a + b > c and a + c > b and b + c > a: # существует ли треугольник?
#         print("triangle is exist")
#     else:
#         print("triangle is not exist")
#
# a = 1
# b = 2
# c = 1
# is_valid_triangle(a, b, c)




#—------------------------------- Задача —--------------------------------#
# Напишите функцию для вычисления площади треугольника (формула Герона)
# def triangle_area(a, b, c):
#    p = (a + b + c) / 2
#    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#    print(area)
#
#
# a = int(input("Введите сторону А: "))
# b = int(input("Введите сторону B: "))
# c = int(input("Введите сторону C: "))
# triangle_area(a, b, c)



#—------------------------------- Задача —--------------------------------#
# Сделайте функцию, которая будет возвращать сколько дней осталось
# до ближайшего 29 февраля.


# что надо знать?
# текущую дату (день, месяц, год)
# дату следующего 29 февраля
def next_29_02(day, month, year):
   days = 0
   if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
      if month == 1:
         days = (31 - day) + 28# 31 - текущий день +  28 февраля
      elif month == 2:
         days = 29 - day
      else:
         days = 3 * 365 + (31 + 28)
         if month == 3:
            days += (31 - day) + (5*31 + 4*30)
         elif month == 4:
            days += (30 - day) + (5 * 31 + 3 * 30)
         elif month == 5:
            days += (31 - day) + (4 * 31 + 3 * 30)
         elif month == 6:
            days += (30 - day) + (4 * 31 + 2 * 30)
         elif month == 7:
            days += (31 - day) + (3 * 31 + 2 * 30)
         elif month == 8:
            days += (31 - day) + (2 * 31 + 2 * 30)
         elif month == 9:
            days += (30 - day) + (2 * 31 + 1 * 30)
         elif month == 10:
            days += (31 - day) + (1 * 31 + 1 * 30)
         elif month == 11:
            days += (30 - day) + (1 * 31 + 0 * 30)
         elif month == 12:
            days += (31 - day) + (0 * 31 + 0 * 30)

   else:
      next_leap_year = 4 - year % 4 - 1
      days = next_leap_year * 365 + (31 + 28)
      if month == 1:
         days += (31 - day) + (6 * 31 + 4 * 30 + 28)
      if month == 2:
         days += (28 - day) + (6 * 31 + 4 * 30)
      if month == 3:
         days += (31 - day) + (5 * 31 + 4 * 30)
      elif month == 4:
         days += (30 - day) + (5 * 31 + 3 * 30)
      elif month == 5:
         days += (31 - day) + (4 * 31 + 3 * 30)
      elif month == 6:
         days += (30 - day) + (4 * 31 + 2 * 30)
      elif month == 7:
         days += (31 - day) + (3 * 31 + 2 * 30)
      elif month == 8:
         days += (31 - day) + (2 * 31 + 2 * 30)
      elif month == 9:
         days += (30 - day) + (2 * 31 + 1 * 30)
      elif month == 10:
         days += (31 - day) + (1 * 31 + 1 * 30)
      elif month == 11:
         days += (30 - day) + (1 * 31 + 0 * 30)
      elif month == 12:
         days += (31 - day) + (0 * 31 + 0 * 30)

   print(f"следующее 29/02  будет через {days} дней")
# from datetime import *
# print(type(datetime.now().day))
# day = datetime.now().day
# month = datetime.now().month
# year = datetime.now().year
#
# next_29_02(28, 2, 2027)
# next_29_02(day, month, year)



# --------------------------------Задача----------------------------------------- #
# напишите функцию для перевода из (км, м, см)  в (км, м, см)
def converter_length(start, end, value):
   if start == 'км':
      start = 3
   elif start == 'м':
      start = 2
   elif start == 'см':
      start = 1
   if end == 'км':
      end == 3
   elif end == 'м':
      end = 2
   elif end == 'см':
      end = 1
   if start == end:
      print(f"ваш длина составляет {value} ")
   #print(f"ваш длина составляет {value} ")

converter_length('м', 'м', 1000)