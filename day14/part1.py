rocks = [list(l) for l in open(0).read().splitlines()]


def roll(rocks):
    while True:
        moved = False
        for r in range(1, len(rocks)):
            for c in range(len(rocks[r])):
                if rocks[r][c] == 'O' and rocks[r-1][c] == '.':
                    rocks[r][c] = '.'
                    rocks[r-1][c] = 'O'
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


print(load(roll(rocks)))
