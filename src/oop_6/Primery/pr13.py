from dataclasses import dataclass

@dataclass(order=True)
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'

queen_of_hearts = PlayingCard('Q', 'v')
ace_of_spades = PlayingCard('A', 'o')
print(ace_of_spades > queen_of_hearts)