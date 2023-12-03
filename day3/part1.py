import re


with open('input.txt') as f:
    data = [line.strip() for line in f.readlines()]

sum = 0

for i, line in enumerate(data):
    for it in re.finditer('[\d]+', line):
        is_valid = False
        for c in range(max(0, it.start() - 1), min(len(line) - 1, it.end() + 1)):
            for l in range(max(0, i - 1), min(len(data) - 1, i + 2)):
                if not (it.start() <= c < it.end() and l == i) and (data[l][c] != '.' and not data[l][c].isdigit()):
                    is_valid = True
                    break
            if is_valid:
                break
        if is_valid:
            sum += int(line[it.start():it.end()])

print(sum)
