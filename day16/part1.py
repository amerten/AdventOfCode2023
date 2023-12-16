import sys

sys.setrecursionlimit(5000)

with open('input.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]

seen = set()
energized = set()


def explore(pos, dir):
    next_pos = (pos[0] + dir[0], pos[1] + dir[1])
    if (pos, next_pos) in seen or next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= len(grid) or next_pos[1] >= len(grid[0]):
        return
    seen.add((pos, next_pos))
    energized.add(next_pos)
    if grid[next_pos[0]][next_pos[1]] == '/':
        if dir == (1, 0):
            explore(next_pos, (0, -1))
        elif dir == (-1, 0):
            explore(next_pos, (0, 1))
        elif dir == (0, 1):
            explore(next_pos, (-1, 0))
        else:
            explore(next_pos, (1, 0))
    elif grid[next_pos[0]][next_pos[1]] == '\\':
        if dir == (1, 0):
            explore(next_pos, (0, 1))
        elif dir == (-1, 0):
            explore(next_pos, (0, -1))
        elif dir == (0, 1):
            explore(next_pos, (1, 0))
        else:
            explore(next_pos, (-1, 0))
    elif grid[next_pos[0]][next_pos[1]] == '-' and (dir == (1, 0) or dir == (-1, 0)):
        explore(next_pos, (0, -1))
        explore(next_pos, (0, 1))
    elif grid[next_pos[0]][next_pos[1]] == '|' and (dir == (0, 1) or dir == (0, -1)):
        explore(next_pos, (1, 0))
        explore(next_pos, (-1, 0))
    else:
        explore(next_pos, dir)


explore((0, -1), (0, 1))
print(len(energized))