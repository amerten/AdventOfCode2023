rocks = [list(l) for l in open(0).read().splitlines()]


def print_rocks(rocks):
    for r in range(len(rocks)):
        print(''.join(rocks[r]))


def my_hash(rocks):
    s = ""
    for line in rocks:
        s += ''.join(line)
    return hash(s)


def cycle(rocks):
    roll(rocks, (-1, 0))
    roll(rocks, (0, -1))
    roll(rocks, (1, 0))
    roll(rocks, (0, 1))


def roll(rocks, direction):
    r_min = 1 if direction[0] == -1 else len(rocks) - 2 if direction[0] == 1 else 0
    r_max = len(rocks) if direction[0] == -1 else -1 if direction[0] == 1 else len(rocks)
    r_delta = 1 if r_min < r_max else -1
    c_min = 1 if direction[1] == -1 else len(rocks[0]) - 2 if direction[1] == 1 else 0
    c_max = len(rocks[0]) if direction[1] == -1 else -1 if direction[1] == 1 else len(rocks[0])
    c_delta = 1 if c_min < c_max else -1
    while True:
        moved = False
        for r in range(r_min, r_max, r_delta):
            for c in range(c_min, c_max, c_delta):
                if rocks[r][c] == 'O' and rocks[r + direction[0]][c + direction[1]] == '.':
                    rocks[r][c] = '.'
                    rocks[r + direction[0]][c + direction[1]] = 'O'
                    moved = True
        if not moved:
            break
    return rocks


def load(rocks):
    t = 0
    for r in range(len(rocks)):
        for c in range(len(rocks[r])):
            if rocks[r][c] == 'O':
                t += (len(rocks) - r)
    return t


seen = []
loads = []
nb_cycles = 1000000000
for i in range(nb_cycles):
    cycle(rocks)
    h = my_hash(rocks)
    if h in seen:
        seen_i = seen.index(h)
        print(loads[seen_i + (nb_cycles - 1 - i) % (i - seen_i)])
        break
    seen.append(h)
    loads.append(load(rocks))
