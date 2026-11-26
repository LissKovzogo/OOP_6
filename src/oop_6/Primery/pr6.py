from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

print(Position('Null Island'))

print(Position('Greenwich', lat=51.8))

print(Position('Vancouver', -123.1, 49.3))
