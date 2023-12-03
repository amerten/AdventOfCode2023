import re


with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

gears = {}

for i, line in enumerate(data):
    for it in re.finditer('[\d]+', line):
        gear_found = False
        for c in range(max(0, it.start() - 1), min(len(line) - 1, it.end() + 1)):
            for l in range(max(0, i - 1), min(len(data) - 1, i + 2)):
                if not (it.start() <= c < it.end() and l == i) and (data[l][c] == '*'):
                    gear_found = True
                    if (l, c) not in gears:
                        gears[(l, c)] = []
                    gears[(l, c)].append(int(it.group()))
                    break
            if gear_found:
                break

print(sum([gears[p][0] * gears[p][1] for p in gears if len(gears[p]) == 2]))


