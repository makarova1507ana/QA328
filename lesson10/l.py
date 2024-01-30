# class Cat:
#     def __init__(self, name, age):# инициализатор - создавать объект и записывать его поля
#         self.name = name # self.name - поле == атрибут == свойство класса
#         self.age = age # self.age - поле == атрибут == свойство класса
#
# # my_cat - объектом или экземпляром класса
# my_cat = Cat(name="Barsik", age=2)
# print(f"name: {my_cat.name}, age: {my_cat.age}")
#
# # friend_cat - объектом или экземпляром класса
# friend_cat = Cat("Vasya", 5)
# print(f"name: {friend_cat.name}, age: {friend_cat.age}")

# # ----------------------------------------задача-------------------------------------------- #
# # Создайте класс, представляющий товар или продукт,
# # хранящий информацию о его названии, цене, количестве на складе
# class Product:
#     def __init__(self, name, price, count):
#         self.name = name
#         self.price = price
#         self.count = count
# book = Product('book1', 1000, 300)
# apple = Product('apple', 200, 456)
# print(book.name, book.price, book.count)
# print(apple.name, apple.price, apple.count)



# ------------------------------------Задача------------------------------------------ #
# # Страница регистрации пользователя: логин, почта, номер телефона, пароль, подтвердить пароль
# # Протестировать эту форму - создать тестовые данные -> Создать класс пользователь
# class User:
#     def __init__(self, login: str, email: str, phone_number: int, password: str, confirm_password: str):
#         self.login = login
#         self.email = email
#         self.phone_number = phone_number
#         self.password = password
#         self.confirm_password = confirm_password
#
#     def authorization(self):
#         # действия по авторизации
#         pass
# #создать тестовые данные
# #валидный пример
# valid_user = User('login123', 'login123@gmail.com', 9991112223344, 'Password12234','Password12234' )
#
# #невалидный создать тестовые данные
# invalid_user = User('login123', 'login123@gmail.com', 9991112223344, 'Password12234','Password1' )


# -----------------------------------Методы класса---------------------------------------#
# class Cat:
#     def __init__(self, name, age):# инициализатор - создавать объект и записывать его поля
#         self.name = name # self.name - поле == атрибут == свойство класса
#         self.age = age # self.age - поле == атрибут == свойство класса
#
#     def play(self):# метод play
#         print(f'method play(): Я {self.name} играю')
# def play():
#     print('функция: play')
# # my_cat - объектом или экземпляром класса
# my_cat = Cat(name="Barsik", age=2)
# print(f"name: {my_cat.name}, age: {my_cat.age}")
# my_cat.play() # вызов метода - потому что требует объекта для вызова
# play() #функция - потому вызвать можно без объекта
#
# print('-----------------------------------')
#
# # friend_cat - объектом или экземпляром класса
# friend_cat = Cat("Vasya", 5)
# print(f"name: {friend_cat.name}, age: {friend_cat.age}")
# friend_cat.play()

#
# #—------------------------------- Задача —--------------------------------#
# # Создайте класс, представляющий Cat, хранящий информацию о его кличке,
# # настроение, энергию(nickname, mood=50, energy=50)
# # и добавьте методы для редактирования этих параметров:
# # * play:
# #   * mood += 10
# #   * energy -= 5
# # * eat:
# #   * mood += 10
# # * sleep
# #   * energy += 10
# # * miss
# #   * mood -= 5
# class Cat:
#     def __init__(self, name: str):
#         self.__name = name
#         self.__mood = 50
#         self.__energy = 50
#
#     def play(self):
#         self.__mood += 10
#         self.__energy -= 5
#
#     def eat(self):
#         self.__mood += 10
#
#     def sleep(self):
#         self.__energy += 10
#
#     def miss(self):
#         self.__mood -= 5
#
#     def __str__(self):
#         return  f'name: {self.__name} | mood: {self.__mood} | energy: {self.__energy}'
# cat = Cat('Baris')
# # cat2 = Cat('Maya')
# # cat3 = Cat('Night')
# #print(cat)
# # print(cat2)
# # print(cat3)
# print(cat)
# cat.mood = '****'
# print('попытались записать строку в настроение',cat)
# cat.play()
# print(cat)
#
# #-------------#
# # cat.play()
# # print(cat)
# #
# # cat.eat()
# # print(cat)
# #
# # cat.miss()
# # print(cat)
# #
# # cat.sleep()
# # print(cat)








# ------------------------------------примеры организации тестов ---------------------------------------------------#
# import pytest # надо установить
# import requests # надо установить
# можно установить через красную лампочку "install package"
# можно установить через терминал(Terminal) "pip install requests"
# file -> settings -> Project: name_project -> Python Interpreter -> +

# date = "2024-01-30"
# url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
# response = requests.get(url) # requests.get() отправить get запрос
# print(type(response), response.status_code)
#
# # example test
# def test_request_with_valid_date(response):
#     # ожидаемые результат
#     expected_result = range(200, 400)  # 200, 201 ... 398, 399
#     # фактический результат
#     result = response.status_code #одно число
#
#     return result in expected_result # True - passed or False - failed
# #
# print(test_request_with_valid_date(response))



#---------------------pytest--------------------------------#
import pytest # надо установить
import requests # надо установить
#test-suit -> тестовый набор
class Test_param_date:
    # example test-case
    def test_request_with_max_valid_date(self):
        date = "2024-01-30"
        url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
        response = requests.get(url)  # requests.get() отправить get запрос

        # ожидаемые результат
        expected_result = range(200, 400)  # 200, 201 ... 398, 399
        # фактический результат
        result = response.status_code #одно число

    def test_request_with_invalid_date(self):
        date = "30-01-2024"
        url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
        response = requests.get(url)  # requests.get() отправить get запрос

        # ожидаемые результат
        expected_result = range(400, 500)
        # фактический результат
        result = response.status_code  # одно число

        return result in expected_result # True - passed or False - failed

    def test_request_with_valid_date(self):
        date = "2010-06-16"
        url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
        response = requests.get(url)  # requests.get() отправить get запрос

        # ожидаемые результат
        expected_result = range(200, 400)
        # фактический результат
        result = response.status_code  # одно число

        return result in expected_result # True - passed or False - failed


    def test_request_with_min_valid_date(self):
        date = "1995-06-16"
        url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
        response = requests.get(url)  # requests.get() отправить get запрос

        # ожидаемые результат
        expected_result = range(200, 400)
        # фактический результат
        result = response.status_code  # одно число

        return result in expected_result # True - passed or False - failed

class Test_param_start_date_and_end_date:
    # def __init__(self):
    #     self.start_date = "2024-01-29"
    #     self.end_date = "2024-01-30"
    #     self.api_key = "jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla"
    #     self.base_url = "https://api.nasa.gov/planetary/apod"
        def test_base_(self):
            start_date = "2024-01-29"
            end_date = "2024-01-30"
            api_key = "jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla"
            base_url = "https://api.nasa.gov/planetary/apod"
            count_days = 2
            url = f"{base_url}?api_key={api_key}&start_date={start_date}&end_date={end_date}"
            expected_result = {'status-code': range(200, 400), 'count_days': count_days}
            response = requests.get(url)
            result_status_code = response.status_code
            result_count_days = len(list(response.json()))
            result = {'status-code': result_status_code, 'count_days': result_count_days}
            return (result['status-code'] in expected_result['status-code']) and   expected_result['count_days'] == result['count_days']

#--------------------------------------------------------#
# start_date = "2024-01-29"
# end_date = "2024-01-30"
# api_key = "jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla"
# base_url = "https://api.nasa.gov/planetary/apod"
#
#
# count_days = 2
# url = f"{base_url}?api_key={api_key}&start_date={start_date}&end_date={end_date}"
# expected_result = {'status-code': range(200, 400), 'count_days': count_days}
# response = requests.get(url)
# result_status_code = response.status_code
# result_count_days = len(list(response.json()))
# print(result_count_days == count_days)