from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

pos = Position('Oslo', 10.8, 59.9)
print(pos)

print(pos.lat)

print(f'{pos.name} is at {pos.lat}N, {pos.lon}E')