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

# -----------------------------------------------------------------------------------------------

X = 26501365
s = X % len(grid)

x1, x2, x3 = s + 3 * len(grid), s + 4 * len(grid), s + 5 * len(grid)
y1, y2, y3 = compute(grid, start, x1), compute(grid, start, x2), compute(grid, start, x3)

a = (x1 * (y3 - y2) + x2 * (y1 - y3) + x3 * (y2 - y1)) / ((x1 - x2) * (x1 - x3) * (x2 - x3))
b = (y2 - y1) / (x2 - x1) - a * (x1 + x2)
c = y1 - a * x1 * x1 - b * x1

print(int(a * X * X + b * X + c))
