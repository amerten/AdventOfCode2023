import math

with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


def power(line):
    game, cubes = line.split(': ')
    sets = cubes.split('; ')
    nb_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for set in sets:
        for subset in set.split(', '):
            nb, color = subset.split()
            nb_cubes[color] = max(nb_cubes[color], int(nb))
    return math.prod(nb_cubes.values())


print(sum(map(power, data)))
