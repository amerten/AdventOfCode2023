min_r, max_r, min_c, max_c = 0, 0, 0, 0
pos = (0, 0)
shell = {pos}
for line in open(0).read().splitlines():
    dir, d, color = line.split()
    dir = (1, 0) if dir == 'D' else (-1, 0) if dir == 'U' else (0, 1) if dir == 'R' else (0, -1)
    d = int(d)
    for _ in range(d):
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        min_r = min(min_r, pos[0])
        max_r = max(max_r, pos[0])
        min_c = min(min_c, pos[1])
        max_c = max(max_c, pos[1])
        shell.add(pos)

t = len(shell)
for r in range(min_r, max_r + 1):
    inside = False
    for c in range(min_c, max_c + 1):
        if (r, c) in shell:
            print('#', end='')
            if (r - 1, c) in shell:
                inside = not inside
        else:
            print(end=' ')
            t += inside
    print()
print(t)