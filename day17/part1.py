import sys

# sys.setrecursionlimit(100000)

blocks = open(0).read().splitlines()
er, ec = len(blocks) - 1, len(blocks[0]) - 1

best = 1000000000000000000000


def explore(node, visited):
    global best
    hl, d, r, c, dr, dc, f = node
    if (r, c) == (er, ec):
        best = min(best, hl)
        return
    if (r, c) in visited:
        return
    if d < 3 and 0 <= r + dr < len(blocks) and 0 <= c + dc < len(blocks[0]):
        v = visited.union((r, c))
        explore((hl + int(blocks[r + dr][c + dc]), d + 1, r + dr, c + dc, dr, dc, node), v)
    if 0 <= r - dc < len(blocks) and 0 <= c + dr < len(blocks[0]):
        v = visited.union((r, c))
        explore((hl + int(blocks[r - dc][c + dr]), 1, r - dc, c + dr, -dc, dr, node), v)
    if 0 <= r + dc < len(blocks) and 0 <= c - dr < len(blocks[0]):
        v = visited.union((r, c))
        explore((hl + int(blocks[r + dc][c - dr]), 1, r + dc, c - dr, dc, -dr, node), v)


explore((0, 0, 0, 0, 1, 0, None), set())
explore((0, 0, 0, 0, 0, 1, None), set())

print(best)