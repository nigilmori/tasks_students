from collections import UserList
import typing as tp

# https://github.com/python/mypy/issues/5264#issuecomment-399407428
if tp.TYPE_CHECKING:
    BaseList = UserList[tp.Optional[tp.Any]]
else:
    BaseList = UserList


class ListTwist(BaseList):
    """
    List-like class with additional attributes:
        * reversed, R - return reversed list
        * first, F - insert or retrieve first element;
                     Undefined for empty list
        * last, L -  insert or retrieve last element;
                     Undefined for empty list
        * size, S -  set or retrieve size of list;
                     If size less than list length - truncate to size;
                     If size greater than list length - pad with Nones
    """
    @property
    def reversed(self) -> tp.Any:
        return self[::-1]

    @property
    def R(self) -> tp.Any:
        return self[::-1]

    @property
    def first(self) -> tp.Any:
        return self[0]

    @first.setter
    def first(self, value: tp.Any) -> tp.Any:
        self[0] = value

    @property
    def F(self) -> tp.Any:
        return self[0]

    @F.setter
    def F(self, value: tp.Any) -> tp.Any:
        self[0] = value

    @property
    def last(self) -> tp.Any:
        return self[-1]

    @last.setter
    def last(self, value: tp.Any) -> tp.Any:
        self[-1] = value

    @property
    def L(self) -> tp.Any:
        return self[-1]

    @L.setter
    def L(self, value: tp.Any) -> tp.Any:
        self[-1] = value

    @property
    def size(self) -> tp.Any:
        return len(self)

    @size.setter
    def size(self, value: tp.Any) -> tp.Any:
        while len(self) > value:
            self.pop()
        while len(self) < value:
            self.append(None)

    @property
    def S(self) -> tp.Any:
        return len(self)

    @S.setter
    def S(self, value: tp.Any) -> tp.Any:
        while len(self) > value:
            self.pop()
        while len(self) < value:
            self.append(None)
