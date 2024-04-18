"""Напишите однострочный генератор словаря, который принимает на вход 
три списка одинаковой длины: имена str, ставка int, премия str 
с указанием процентов вида “10.25%”. В результате получаем словарь с 
именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии"""

names = ['Alex', 'Ford', "Elena"]
salaries = [10000, 50000, 25000]
awards = ['10.5%', '7.3%', '5%' ]


def calc_bonus(name: list[str], salary: list[int], award: list[str]) -> dict[str, float]:
    result = {}
    for name, salary, award in zip(names, salaries, awards):
        bonus_amount = salary * float(award[:-1]) / 100
        result[name] = bonus_amount
    return result


print(calc_bonus(names, salaries, awards))