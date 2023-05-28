import typing as tp


def filter_list_by_list(lst_a: tp.Union[list[int], range], lst_b: tp.Union[list[int], range]) -> list[int]:
    i, j = 0, 0
    otv = []
    while (i < len(lst_a)) and (j < len(lst_b)):
        if lst_a[i] == lst_b[j]:
            i += 1
        elif lst_a[i] < lst_b[j]:
            otv.append(lst_a[i])
            i += 1
        else:
            j += 1
    while i < len(lst_a):
        otv.append(lst_a[i])
        i += 1
    return otv
