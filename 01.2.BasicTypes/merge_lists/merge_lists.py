def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    i, j, otv = 0, 0, []
    while i < len(lst_a) and j < len(lst_b):
        if lst_a[i] < lst_b[j]:
            otv.append(lst_a[i])
            i += 1
        else:
            otv.append(lst_b[j])
            j += 1
    if i == len(lst_a):
        while j < len(lst_b):
            otv.append(lst_b[j])
            j += 1
    else:
        while i < len(lst_a):
            otv.append(lst_a[i])
            i += 1
    return otv


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    return sorted(lst_a+lst_b)
