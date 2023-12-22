def compute(grid, start, nb_steps):
    tiles = {start}
    for _ in range(nb_steps):
        new_tiles = set()
        for tile in tiles:
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = tile[0] + d[0], tile[1] + d[1]
                mr, mc = r % len(grid), c % len(grid)
                if grid[mr][mc] != '#':
                    new_tiles.add((r, c))
        tiles = new_tiles
    return len(tiles)


start = (0, 0)
grid = []
for r, line in enumerate(open(0).read().splitlines()):
    row = list(line.strip())
    if 'S' in row:
        c = row.index('S')
        row[c] = '.'
        start = (r, c)
    grid.append(row)
print(len(grid))
t = []
s = 5000 % len(grid)
for i in range(3):
    t.append(compute(grid, start, s + i * len(grid)))
fx, fy, fz = t[0], t[1], t[2]
x, y, z = s, s + len(grid), s + 2 * len(grid)

for a in range(100):
    for b in range(100):
        for c in range(100):
            if a*x*x + b*x + c == fx and a*y*y + b*y + c == fy and a*z*z + b*z + c == fz:
                print(a, b, c)