import sys

sys.setrecursionlimit(10000)

grid = open(0).read().splitlines()

distances = []


def walk(r, c, seen):
    global distances
    if r == len(grid) - 1 and c == len(grid[0]) - 2:
        distances.append(len(seen))
        return
    if (r, c) in seen:
        return
    nseen = seen.copy()
    nseen.add((r, c))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if grid[r][c] != '.':
        directions = [directions['v^><'.index(grid[r][c])]]
    for direction in directions:
        nr, nc = r + direction[0], c + direction[1]
        if 0 <= nr < len(grid) and 0 <= c < len(grid[0]) and grid[nr][nc] != '#':
            walk(nr, nc, nseen)


walk(0, 1, set())
print(max(distances))
