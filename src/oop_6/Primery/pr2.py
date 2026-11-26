class RegularCard:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts.rank)

print(queen_of_hearts)

print(queen_of_hearts == RegularCard('Q', 'Hearts'))