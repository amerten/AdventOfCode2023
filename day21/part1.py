start = (0, 0)
grid = []
for r, line in enumerate(open(0).read().splitlines()):
    row = list(line.strip())
    if 'S' in row:
        c = row.index('S')
        row[c] = '.'
        start = (r, c)
    grid.append(row)

nb_steps = 64
tiles = {start}
for _ in range(nb_steps):
    new_tiles = set()
    for tile in tiles:
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = tile[0] + d[0], tile[1] + d[1]
            if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] != '#':
                new_tiles.add((r, c))
    tiles = new_tiles
print(len(tiles))
