def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    otv = [a, b, c]
    otv.remove(max(otv))
    otv.remove(min(otv))
    return otv[0]
