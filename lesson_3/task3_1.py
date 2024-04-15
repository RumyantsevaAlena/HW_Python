"""Дан список повторяющихся элементов. Вернуть список с дублирующимися
 элементами. В результирующем списке не должно быть дубликатов."""


def find_duplicat(lst):
    return list(set([x for x in l_st if l_st.count(x) > 1]))


l_st = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(find_duplicat(l_st))