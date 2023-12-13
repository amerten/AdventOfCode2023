grids = [g.splitlines() for g in open(0).read().split('\n\n')]


def value(grid):
    for r in range(1, len(grid)):
        size = min(r, len(grid) - r)
        for i in range(size):
            if grid[r - i - 1] == grid[r + i]:
                continue
            else:
                break
        else:
            return 100 * r
    for c in range(1, len(grid[0])):
        size = min(c, len(grid[0]) - c)
        for i in range(size):
            if list(zip(*grid))[c - i - 1] == list(zip(*grid))[c + i]:
                continue
            else:
                break
        else:
            return c
    return 0


print(sum(map(value, grids)))
