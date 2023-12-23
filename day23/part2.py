import sys

sys.setrecursionlimit(10000)

grid = open(0).read().splitlines()
crossroads = {}
seen = set()


def find_crossroads(r, c, d, prev):
    if (r, c) in seen and ((r, c) not in crossroads or (r, c) == prev):
        return
    if (r, c) == (len(grid) - 1, len(grid[0]) - 2):
        crossroads[prev][(len(grid) - 1, len(grid[0]) - 2)] = d
        return
    seen.add((r, c))
    nb_roads = 0
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= nr < len(grid) and 0 <= c < len(grid[0]) and grid[nr][nc] != '#':
            nb_roads += 1
    if nb_roads > 2:
        if (r, c) not in crossroads:
            crossroads[(r, c)] = {}
        if prev not in crossroads:
            crossroads[prev] = {}
        crossroads[(r, c)][prev] = d
        crossroads[prev][(r, c)] = d
        prev = (r, c)
        d = 0
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if 0 <= nr < len(grid) and 0 <= c < len(grid[0]) and grid[nr][nc] != '#':
            find_crossroads(nr, nc, d + 1, prev)


find_crossroads(0, 1, 0, (0, 1))

path_l = 0


def walk(p, d, path):
    global path_l
    if p == (len(grid) - 1, len(grid[0]) - 2):
        path_l = max(path_l, d)
        return
    if p in path:
        return
    v = path.copy()
    v.append(p)
    for dest in crossroads[p]:
        walk(dest, d + crossroads[p][dest], v)


walk((0, 1), 0, [])
print(path_l)
