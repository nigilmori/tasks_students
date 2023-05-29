from typing import Iterable, Generator, Any


def flat_it(sequence: Iterable[Any]) -> Generator[Any, None, None]:
    """
    :param sequence: sequence with arbitrary level of nested iterables
    :return: generator producing flatten sequence
    """
    for i in sequence:
        if hasattr(i, "__iter__"):
            if type(i) == str and len(i) == 1:
                yield i[0]
            else:
                for j in flat_it(i):
                    yield j
        else:
            yield i
