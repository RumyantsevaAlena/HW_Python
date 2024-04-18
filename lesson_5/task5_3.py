"""Создайте функцию генератор чисел Фибоначчи """


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


a = int(input('введите число  '))
print (list(fibonacci(a)))