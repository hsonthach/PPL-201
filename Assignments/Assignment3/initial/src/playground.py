from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple

from functools import reduce


class Element(ABC):
    pass


@dataclass
class Many(Element):
    value: List[Element]
    pass


@dataclass
class Int(Element):
    value: int
    pass


@dataclass
class Float(Element):
    value: float
    pass


many = [Many([Int(3), Many([Float(2.1), Int(5)]), Float(1.0), Int(2), Many(
    [Int(3), Many([Float(2.1), Int(5)]), Float(1.0), Int(2)])]), Int(1)]


def f(a: Element):
    if (type(a) is Many):
        return reduce(lambda x, y: x + f(y), a.value, 0)
    if (type(a) is Int):
        return 1
    return 0


def sum(lst, f):
    return reduce(lambda a, b: a + f(b), lst, 0)


print(sum(many, f))
