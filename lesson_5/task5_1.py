"""Напишите функцию, которая принимает на вход строку - абсолютный путь 
до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, 
расширение файла."""


import os
string = "C:/АленаРумянцева/Desktop/GreekBrains/ДЗ/Python_advanced/lesson_5/task5_1.py"


def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension


print(f'Кортеж из пути: {fun(string)}')