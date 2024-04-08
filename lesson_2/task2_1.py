"""Напишите программу, которая получает целое число и возвращает его 
шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата."""

BASE = 16

number = int(input('Введите число: '))
print(hex(number))
result = ''
while number > BASE:
    result += str(number % BASE)
    number //= BASE
result += str(number)
print(result[::-1])