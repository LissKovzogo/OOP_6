from dataclasses import dataclass, field
from typing import List

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'
SUITS = '◊ v o'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank)*len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'

queen_of_hearts = PlayingCard('Q', 'v')
ace_of_spades = PlayingCard('A', 'o')
print(ace_of_spades > queen_of_hearts)