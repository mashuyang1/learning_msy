import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
# print(beer_card)
deck = FrenchDeck()
# print(len(deck))
# print(deck[0])
# from random import choice
# print(choice(deck))
# print(deck[:3])
# print(deck[12::13])
# for card in reversed(deck):
#     print(card)
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)  # 创建一个字典
# print(suit_values['spades'])


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)  # 返回Card的rank位置有哪些
    # print(rank_value * len(suit_values) + suit_values[card.suit])
    print(suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):  # 为什么用deck而不是Card，元祖Card是没有迭代方法的，对象deck有
    print(card)
