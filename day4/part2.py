with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


def nb_wins(line):
    card, nbs = line.split(': ')
    winning, my_numbers = nbs.split(' | ')
    winning = winning.split()
    my_numbers = my_numbers.split()
    return len([n for n in my_numbers if n in winning])


nb_cards = {i + 1: 1 for i in range(len(data))}
for i, line in enumerate(data):
    card_nb = i + 1
    card_nbs = nb_cards[card_nb]
    for j in range(nb_wins(line)):
        next_card = card_nb + j + 1
        if next_card <= len(data):
            nb_cards[next_card] += card_nbs

print(sum(nb_cards.values()))

