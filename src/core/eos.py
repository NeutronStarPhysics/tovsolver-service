from collections import MutableSequence
from dataclasses import dataclass
from astropy import units


@dataclass
class EoSElement:
    """Equation of state element"""
    pressure: float
    energy: float


class EoSList(MutableSequence):
    """Equation of state"""

    @classmethod
    def new_instance(cls, unit):
        """Factory method"""
        return cls(unit)

    def __init__(self, unit):
        self.list = list()
        self.unit: units = unit

    def __getitem__(self, i):
        return self.list[i]

    def __delitem__(self, i):
        del self.list[i]

    def __setitem__(self, index, item):
        self.list[index] = item

    def insert(self, index, item):
        """Insert method"""
        self.list.insert(index, item)

    def append(self, item):
        """Append method"""
        self.list.append(item)

    def __str__(self):
        return str(self.list)

    def __len__(self) -> int:
        return len(self.list)
