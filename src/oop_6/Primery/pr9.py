from dataclasses import dataclass
from typing import List

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'
SUITS = '◊'.split()

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

print(make_french_deck())