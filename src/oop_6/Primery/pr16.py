from dataclasses import dataclass

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'
SUITS = '◊ v o'.split()

@dataclass(order=True)
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'

@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str

@dataclass(frozen=True)
class ImmutableDeck:
    cards: list[PlayingCard]

queen_of_hearts = ImmutableCard('Q', 'v')
ace_of_spades = ImmutableCard('A', 'o')
deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
print(deck)

deck.cards[0] = ImmutableCard('7', 'y')
print(deck)