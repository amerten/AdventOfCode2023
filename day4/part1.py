import math


with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


def points(line):
    card, nbs = line.split(': ')
    winning, my_numbers = nbs.split(' | ')
    winning = winning.split()
    my_numbers = my_numbers.split()
    return int(math.pow(2, len([n for n in my_numbers if n in winning]) - 1))


print(sum(map(points, data)))
