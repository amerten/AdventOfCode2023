with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]


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
    if c1 or c2 == '.' or p1 == p2:
        return False
    connected_right = p2 == (p1[0], p1[1] + 1) and c2 in '-7J'
    connected_left = p2 == (p1[0], p1[1] - 1) and c2 in 'FL-'
    connected_bottom = p2 == (p1[0] + 1, p1[1]) and c2 in '|LJ'
    connected_top = p2 == (p1[0] - 1, p1[1]) and c2 in 'F|7'
    if c1 == 'F': return connected_bottom or connected_right
    if c1 == '-': return connected_left or connected_right
    if c1 == '7': return connected_left or connected_bottom
    if c1 == '|': return connected_top or connected_bottom
    if c1 == 'L': return connected_top or connected_right
    if c1 == 'J': return connected_top or connected_left
    raise Exception("Unknown pipe: " + c1)


distances = {}
previous_position, current_position = None, start

print(start)

for dr in range(-1, 2):
    for dc in range(current_position[1] - 1, current_position[1] + 2):
        if (r == 0 and c == 0) or (r != 0 and c != 0):
            continue
        print("Is connected ?" + str((r, c)))
        print(are_connected(current_position, (r, c)))
        if are_connected(current_position, (r, c)):
            previous_position = start
            current_position = (r, c)
            break
    else:
        continue
    break

print(previous_position, current_position)

distance = 1
while current_position != start:
    for dr in range(current_position[0] - 1, current_position[0] + 2):
        for c in range(current_position[1] - 1, current_position[1] + 2):
            if r == 0 and c == 0 or r != 0 and c != 0:
                continue
            if are_connected(previous_position, (r, c)) and (r, c) != previous_position:
                distance += 1
                distances[(r, c)] = distance
                previous_position = current_position
                current_position = (r, c)
                break
        else:
            continue
        break

for p in distances:
    distances[p] = min(distances[p], len(distances) - distances[p])

print(max(distances.values()))
