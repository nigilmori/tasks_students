from math import ceil
from typing import Iterable, Sized, Iterator, Any


class Range(Sized, Iterable[int]):
    """The range-like type, which represents an immutable sequence of numbers"""

    def __init__(self, *args: int) -> None:
        """
        :param args: either it's a single `stop` argument
            or sequence of `start, stop[, step]` arguments.
        If the `step` argument is omitted, it defaults to 1.
        If the `start` argument is omitted, it defaults to 0.
        If `step` is zero, ValueError is raised.
        """
        if len(args) == 1:
            self.start = 0
            self.end = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
            self.step = 1
        else:
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]
        if self.step == 0:
            raise ValueError("range() arg 3 must not be zero")

    def __iter__(self) -> Any:
        return RangeIterator(self)

    def __repr__(self) -> str:
        if self.step == 1:
            return "range" + str((self.start, self.end))
        return "range" + str((self.start, self.end, self.step))

    def __str__(self) -> str:
        if self.step == 1:
            return "range" + str((self.start, self.end))
        return "range" + str((self.start, self.end, self.step))

    def __contains__(self, key: int) -> bool:
        return self.step*self.start <= self.step*key < self.step*self.end and (key-self.start) % self.step == 0

    def __getitem__(self, key: int) -> int:
        if key < (self.end - self.start) // self.step:
            return self.start + self.step*key
        else:
            raise IndexError("range object index out of range")

    def __len__(self) -> int:
        if (self.end - self.start) * self.step < 0:
            return 0
        return ceil((self.end - self.start) / self.step)


class RangeIterator(Iterator[Range]):

    def __init__(self, range: Range) -> None:
        self.range = range
        self.now = self.range.start - self.range.step

    def __iter__(self) -> Iterator[Range]:
        return self

    def __next__(self) -> Any:
        self.now = self.now + self.range.step
        if self.range.step * self.now < self.range.step * self.range.end:
            return self.now
        raise StopIteration
