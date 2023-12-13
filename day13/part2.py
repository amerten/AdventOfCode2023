grids = [[list(l) for l in (g.splitlines())] for g in open(0).read().split('\n\n')]


def value(grid, old_value):
    for r in range(1, len(grid)):
        size = min(r, len(grid) - r)
        for i in range(size):
            if grid[r - i - 1] == grid[r + i]:
                continue
            else:
                break
        else:
            if 100 * r != old_value:
                return 100 * r
            continue
    for c in range(1, len(grid[0])):
        size = min(c, len(grid[0]) - c)
        for i in range(size):
            if list(zip(*grid))[c - i - 1] == list(zip(*grid))[c + i]:
                continue
            else:
                break
        else:
            if c != old_value:
                return c
            continue
    return 0


def real_value(grid):
    old_val = value(grid, -1)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] = "." if grid[r][c] == "#" else "#"
            new_val = value(grid, old_val)
            grid[r][c] = "." if grid[r][c] == "#" else "#"
            if new_val != 0:
                return new_val


print(sum(map(real_value, grids)))
