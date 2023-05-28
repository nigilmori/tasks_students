import math
from dataclasses import dataclass, field, InitVar
from abc import ABC, abstractmethod

DISCOUNT_PERCENTS = 15


@dataclass(frozen=True, order=True)
class Item:
    # note: mind the order of fields (!)
    item_id: int = field(compare=False)
    title: str = field()
    cost: int = field()

    def __post_init__(self) -> None:
        assert self.cost > 0, "Cost must be positive"
        assert len(self.title) > 0, "Title must be"


# Do not remove `# type: ignore`
# It is [a really old issue](https://github.com/python/mypy/issues/5374)
@dataclass  # type: ignore
class Position(ABC):
    item: Item

    @property
    @abstractmethod
    def cost(self) -> None:
        pass


@dataclass
class CountedPosition(Position):
    count: int = 1

    @property
    def cost(self):  # type: ignore
        return self.item.cost * self.count


@dataclass
class WeightedPosition(Position):
    weight: float = 1.0

    @property
    def cost(self):  # type: ignore
        return self.item.cost * self.weight


@dataclass
class Order:
    order_id: int
    positions: list[Position] = field(default_factory=list)
    cost: int = field(init=False)
    have_promo: InitVar[bool] = False

    def __post_init__(self, have_promo):  # type: ignore
        self.cost = (math.floor(sum([position.cost for position in self.positions]) -
                     sum([position.cost for position in self.positions])*0.15*int(have_promo))
                     if self.positions is not None else 0)
