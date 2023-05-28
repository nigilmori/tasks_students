import typing as tp


def get_fizz_buzz(n: int) -> list[tp.Union[int, str]]:
    """
    If value divided by 3 - "Fizz",
       value divided by 5 - "Buzz",
       value divided by 15 - "FizzBuzz",
    else - value.
    :param n: size of sequence
    :return: list of values.
    """
    otv: list[tp.Union[int, str]] = []
    for i in range(n):
        if (i + 1) % 15 == 0:
            otv.append("FizzBuzz")
        elif (i + 1) % 5 == 0:
            otv.append("Buzz")
        elif (i + 1) % 3 == 0:
            otv.append("Fizz")
        else:
            otv.append(int(i + 1))
    return otv
