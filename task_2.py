"""Напишите код, который запрашивает число и сообщает 
является ли оно простым или составным. Используйте правило
для проверки: “Число является простым, если делится нацело 
только на единицу и на себя”. Сделайте ограничение на ввод 
отрицательных чисел и чисел больше 100 тысяч"""

IGNORE_1 = 0
IGNORE_2 = 100000
numb = int(input("Введите число: "))
count = 0
if numb < IGNORE_1 or numb > IGNORE_2:
    print("Это число не подходит, попробуйте другое")
else:
    if numb == 0 or numb == 1:
        print("Число не является простым и составным")
    for i in range(2, numb // 2 + 1):
        if numb % i == 0:
            count += 1
    if count <= 0:
        print("Число простое")
    else:
        print("Число составное")