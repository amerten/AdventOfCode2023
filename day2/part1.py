with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


def is_possible(line, red=12, green=13, blue=14):
    game, cubes = line.split(': ')
    game_id = int(game.split()[1])
    sets = cubes.split('; ')
    for set in sets:
        for subset in set.split(', '):
            nb, color = subset.split()
            if color == 'red' and int(nb) > red:
                return 0
            if color == 'green' and int(nb) > green:
                return 0
            if color == 'blue' and int(nb) > blue:
                return 0
    return game_id


print(sum(map(is_possible, data)))
