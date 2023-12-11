with open('input.txt') as f:
    data = [list(line.strip()) for line in f.readlines()]

for r in range(len(data)):
    for c in range(len(data)):
        if data[r][c] == 'S':
            start = (r, c)
            break
    else:
        continue
    break


def are_connected(p1, p2):
    c1, c2 = data[p1[0]][p1[1]], data[p2[0]][p2[1]]
    if c1 == '.' or c2 == '.' or p1 == p2:
        return False
    connected_right = p2 == (p1[0], p1[1] + 1) and c2 in '-7JS'
    connected_left = p2 == (p1[0], p1[1] - 1) and c2 in 'FL-S'
    connected_bottom = p2 == (p1[0] + 1, p1[1]) and c2 in '|LJS'
    connected_top = p2 == (p1[0] - 1, p1[1]) and c2 in 'F|7S'
    if c1 == 'F': return connected_bottom or connected_right
    if c1 == '-': return connected_left or connected_right
    if c1 == '7': return connected_left or connected_bottom
    if c1 == '|': return connected_top or connected_bottom
    if c1 == 'L': return connected_top or connected_right
    if c1 == 'J': return connected_top or connected_left
    return connected_top or connected_bottom or connected_right or connected_left


loop = []
previous_position, current_position = None, start

while True:
    for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        r, c = current_position[0] + d[0], current_position[1] + d[1]
        if r < 0 or r >= len(data) or c < 0 or c >= len(data[r]):
            continue
        if are_connected(current_position, (r, c)) and (r, c) != previous_position:
            previous_position = current_position
            current_position = (r, c)
            loop.append(previous_position)
            break
    if current_position == start:
        break

a, b = loop[1], loop[-1]
if a[0] == start[0] + 1:  # a is below
    if b[1] == start[1] - 1:  # b to left
        s = "7"
    elif b[1] == start[1] + 1:  # b to right
        s = "F"
    else:
        s = "|"
elif a[0] == start[0] - 1:  # a on top
    if b[1] == start[1] - 1:  # b to left
        s = "J"
    elif b[1] == start[1] + 1:  # b to right
        s = "L"
    else:
        s = "|"
elif a[1] == start[0] + 1:  # a on right
    if b[1] == start[1] - 1:  # b to left
        s = "-"
    elif b[0] == start[0] - 1:  # b on top
        s = "L"
    else:
        s = "F"
else:  # a is on left
    if b[1] == start[1] + 1:  # b to right
        s = "-"
    elif b[0] == start[0] - 1:  # b on top
        s = "J"
    else:
        s = "7"
data[start[0]][start[1]] = s

t = 0
for r in range(len(data)):
    is_inside = False
    for c in range(len(data[r])):
        if (r, c) in loop:
            if data[r][c] in '|JL':
                is_inside = not is_inside
        else:
            t += is_inside
print(t)