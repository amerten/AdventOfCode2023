min_r, max_r, min_c, max_c = 0, 0, 0, 0
v, h = [], []
r, c = 0, 0
t = 0
for line in open(0).read().splitlines():
    dir, d, color = line.split()
    d = int(d)
    t += d
    if dir == 'R':
        h.append((r, c, c + d))
        c += d
        max_c = max(max_c, c)
    elif dir == 'D':
        v.append((c, r, r + d))
        r += d
        max_r = max(max_r, r)
    elif dir == 'L':
        h.append((r, c - d, c))
        c -= d
        min_c = min(min_c, c)
    else:
        v.append((c, r - d, r))
        r -= d
        min_r = min(min_r, r)

v.sort()
h.sort()

for r in range(min_r, max_r + 1):
    inside = False
    prev_crossed = None
    for i, l in enumerate(v):
        was_inside = inside
        if l[1] + 1 <= r <= l[2]:
            inside = not inside
        if l[1] <= r <= l[2]:
            if was_inside:
                for hl in h:
                    if hl[0] == r and hl[1] <= l[0] - 1 <= hl[2]:
                        break
                else:
                    t += (l[0] - prev_crossed[0] - 1)
            prev_crossed = l
print(t)