import typing as tp
import heapq


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    mins = [[seq[i][0], i, 0] for i in range(len(seq)) if len(seq[i]) > 0]
    heapq.heapify(mins)
    otv = []
    while len(mins) > 0:
        mini = heapq.heappop(mins)
        otv.append(mini[0])
        if mini[2] < len(seq[mini[1]]) - 1:
            heapq.heappush(mins, [seq[mini[1]][mini[2]+1], mini[1], mini[2]+1])
    return otv
