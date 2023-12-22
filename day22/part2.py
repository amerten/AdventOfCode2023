def list_points(p1, p2):
    if p1[0] != p2[0]:
        delta = 1 if p1[0] < p2[0] else -1
        nbp = abs(p1[0] - p2[0]) + 1
        return list(zip(list(range(p1[0], p2[0] + delta, delta)), [p1[1]] * nbp, [p1[2]] * nbp))
    elif p1[1] != p2[1]:
        delta = 1 if p1[1] < p2[1] else -1
        nbp = abs(p1[1] - p2[1]) + 1
        return list(zip([p1[0]] * nbp, list(range(p1[1], p2[1] + delta, delta)), [p1[2]] * nbp))
    else:
        delta = 1 if p1[2] < p2[2] else -1
        nbp = abs(p1[2] - p2[2]) + 1
        return list(zip([p1[0]] * nbp, [p1[1]] * nbp, list(range(p1[2], p2[2] + delta, delta))))


bricks = [[0]]  # the ground
id = 1
for line in open(0).read().splitlines():
    x1, y1, z1, x2, y2, z2 = (list(map(int, line.replace('~', ',').split(','))))
    if z1 <= z2:
        bricks.append([z1, y1, x1, z2, y2, x2, id])
    else:
        bricks.append([z2, y2, x2, z1, y1, x1, id])
    id += 1

bricks.sort()

for i, b in enumerate(bricks[1:]):
    move_dist = 1000
    line_1 = list_points(b[:3], b[3:6])
    for j, ob in enumerate(bricks[:i + 1]):
        if ob == [0]:  # the ground
            assert j == 0
            move_dist = line_1[0][0] - 1
        else:
            line_2 = list_points(ob[:3], ob[3:6])
            for p1 in line_1:
                for p2 in line_2:
                    if p1[1] == p2[1] and p1[2] == p2[2]:
                        move_dist = min(move_dist, abs(p1[0] - p2[0]) - 1)
    b[0] -= move_dist
    b[3] -= move_dist

blocked_by = {}
who_blocks_who = {}
for i, b in enumerate(bricks[1:]):
    for ob in bricks[i + 2:]:
        blocks = False
        for p1 in list_points(b[:3], b[3:6]):
            for p2 in list_points(ob[:3], ob[3:6]):
                if p1[1] == p2[1] and p1[2] == p2[2]:
                    if p1[0] == p2[0] + 1:
                        blocks, blocker, blocked = True, ob[6], b[6]
                    elif p2[0] == p1[0] + 1:
                        blocks, blocker, blocked = True, b[6], ob[6]
                    if blocks:
                        if blocker not in who_blocks_who:
                            who_blocks_who[blocker] = set()
                        if blocked not in blocked_by:
                            blocked_by[blocked] = set()
                        who_blocks_who[blocker].add(blocked)
                        blocked_by[blocked].add(blocker)
                        break
            if blocks:
                break


t = 0
for i in range(id):
    felt = {i}
    while True:
        l = len(felt)
        for j in range(id):
            if j in blocked_by:
                if blocked_by[j].intersection(felt) == blocked_by[j]:
                    felt.add(j)
        if len(felt) == l:
            break
    t += (len(felt) - 1)
print(t)
