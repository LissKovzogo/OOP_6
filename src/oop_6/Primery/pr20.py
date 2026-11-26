from dataclasses import dataclass
from timeit import timeit

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float

simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('Madrid', -3.7, 40.4)
timeit('slot.name', setup="from position import SlotPosition; "
                          "slot = SlotPosition('Oslo', 10.8, 59.9)")
