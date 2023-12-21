from heapq import heappush, heappop

grid = open(0).read().splitlines()
end = len(grid) - 1, len(grid[0]) - 1

visited = set()
queue = [(0, 0, 0, 0, 1, 0)]
while queue:
    hl, r, c, dr, dc, d = heappop(queue)

    if (r, c) == end and d >= 4:
        print(hl)
        break

    if (r, c, dr, dc, d) in visited:
        continue

    visited.add((r, c, dr, dc, d))

    nr, nc = r + dr, c + dc
    if d < 10 and 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        new_node = (hl + int(grid[nr][nc]), nr, nc, dr, dc, d + 1)
        heappush(queue, new_node)

    if d >= 4 or hl == 0:
        lr, lc = r - dc, c + dr
        if 0 <= lr < len(grid) and 0 <= lc < len(grid[0]):
            new_node = (hl + int(grid[lr][lc]), lr, lc, -dc, dr, 1)
            heappush(queue, new_node)
        rr, rc = r + dc, c - dr
        if 0 <= rr < len(grid) and 0 <= rc < len(grid[0]):
            new_node = (hl + int(grid[rr][rc]), rr, rc, dc, -dr, 1)
            heappush(queue, new_node)
