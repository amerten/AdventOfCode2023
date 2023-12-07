with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class Hand:
    def __init__(self, cards, bid):
        self._cards = cards
        self._bid = int(bid)

    def cards(self):
        return self._cards

    def bid(self):
        return self._bid

    def hand_type(self):
        m = {}
        for c in self._cards:
            if c not in m:
                m[c] = 0
            m[c] += 1
        for c, nb in m.items():
            if nb == 5:
                return 6
            elif nb == 4:
                return 5
            elif nb == 3:
                return 4 if len(m) == 2 else 3
            elif nb == 2:
                return 4 if len(m) == 2 else 2 if len(m) == 3 else 1
        return 0

    def __lt__(self, other):
        if self.hand_type() != other.hand_type():
            return self.hand_type() < other.hand_type()
        for i, c in enumerate(self._cards):
            if c != other.cards()[i]:
                return CARDS.index(c) > CARDS.index(other.cards()[i])
        return 0

    def __hash__(self):
        return hash(self._cards)

    def __str__(self):
        return self._cards


hands = []
for line in data:
    hands.append(Hand(*line.split()))
hands.sort()

print(sum([h.bid() * (i+1) for i, h in enumerate(hands)]))